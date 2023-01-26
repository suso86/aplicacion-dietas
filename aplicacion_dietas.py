from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from werkzeug.utils import secure_filename
from os import remove
from datetime import timedelta

from cliente import Cliente
import funciones

#hola
app=Flask(__name__)

#Variable para recoger los datos mientras se registra un cliente
cliente = Cliente()

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        global cliente
        cliente.kcal = request.form['kcal']
        cliente.proteinas = request.form['proteinas']
        cliente.grasas = request.form['grasas'] 
        cliente.hc = request.form['hc']

    return render_template("base.html")

#-------------------------------------------------------------------------------------#
#Parte de la entrevista 
@app.route("/registro_cliente")
def Entrevista():
    return render_template("datos_basicos.html")

@app.route("/registro_cliente/antecedentes", methods=["POST"])
def SaludAntecedentes():
    global cliente
    if request.method == "POST":
        cliente.nombre = request.form['nombre_cliente']
        cliente.primer_apellido = request.form['primer_apellido']
        cliente.segundo_apellido = request.form['segundo_apellido']
        cliente.direccion = request.form['direccion_cliente']
        cliente.edad = request.form['edad_cliente']
        cliente.sexo = request.form['hm_cliente']
        cliente.telefono = request.form['numero_tlf']
        cliente.motivo_consulta = request.form['motivo_consulta']

        return render_template("datos_clinicos.html")

@app.route("/registro_cliente/habitos", methods=["POST"])
def HabitosAlimenticios():
    global cliente
    if request.method == "POST":
        cliente.sn_cliente_enfermedad = request.form['sn_cliente_enfermedad']
        cliente.cual_enfermedad = request.form['cual_enfermedad']
        cliente.sn_cliente_alergia = request.form['sn_cliente_alergia']
        cliente.cual_alergia = request.form['cual_alergia']
        cliente.sn_cliente_antecedentes = request.form['sn_cliente_antecedentes']
        cliente.cual_antecedentes = request.form['cual_antecedentes']
        cliente.sn_cliente_estreñimiento = request.form['sn_cliente_estreñimiento']
        cliente.cual_estreñimiento = request.form['cual_estreñimiento']
        cliente.sn_cliente_hormonal = request.form['sn_cliente_hormonal']
        cliente.cual_hormonal = request.form['cual_hormonal']
        
        return render_template("habitos_alimenticios.html")

@app.route("/registro_cliente/estilo", methods=["POST"])
def EstiloVida():
    global cliente
    if request.method == "POST":
        cliente.verdura_fruta = request.form['verdura_fruta']
        cliente.legumbres_cereales = request.form['legumbres_cereales']
        cliente.pescado_carne = request.form['pescado_carne']
        cliente.frutos_secos = request.form['frutos_secos']
        cliente.lacteos = request.form['lacteos']
        cliente.aceite = request.form['aceite']
        cliente.preparar_alimentos = request.form['preparar_alimentos']
        cliente.historial = request.form['historial']
        cliente.edad_maxima = request.form['edad_maxima']
        cliente.causa = request.form['causa']
        cliente.sn_cliente_regimen = request.form['sn_cliente_regimen']
        cliente.cual_regimen_nutricional = request.form['cual_regimen_nutricional']

        return render_template("estilo_vida.html")

@app.route("/registro_cliente/evaluacion", methods=["POST"])
def EvaluacionAntropometrica():
    global cliente
    if request.method == "POST":
        cliente.actividad = request.form['actividad']
        cliente.sn_cliente_alcohol = request.form['sn_cliente_alcohol']
        cliente.sn_cliente_cafe = request.form['sn_cliente_cafe']
        cliente.sn_cliente_tabaco = request.form['sn_cliente_tabaco']
        cliente.sueño = request.form['sueño']
        cliente.frecuencia_comida = request.form['frecuencia_comida']
        cliente.encargado_compra = request.form['encargado_compra']
        cliente.frecuencia_compras = request.form['frecuencia_compras']
        cliente.sn_gustar_cocinar = request.form['sn_gustar_cocinar']
        cliente.mas_hambre = request.form['mas_hambre']
        cliente.desayuno_habitual = request.form['desayuno_habitual']
        cliente.merienda_habitual = request.form['merienda_habitual']
        cliente.preferencia_merienda = request.form['preferencia_merienda']
        cliente.preferencia_desayuno = request.form['preferencia_desayuno']
        cliente.platos = request.form['platos']
        cliente.comidas_realizar = request.form.getlist('comidas_realizar')

        return render_template("evaluacion_antropometrica.html")

@app.route("/registro_cliente/requerimientos", methods=["POST"])
def Requerimientos():
    global cliente
    if request.method == "POST":
        cliente.altura = request.form['altura']
        cliente.peso = request.form['peso']
        cliente.graso = request.form['graso']
        cliente.brazo = request.form['brazo']
        cliente.cintura = request.form['cintura']
        cliente.cuadriceps = request.form['cuadriceps']
        cliente.espalda = request.form['espalda']
        cliente.hombro = request.form['hombro']
        cliente.piernas = request.form['piernas']

        #Realizamos en este apartado las funciones para ver los macronutrientes
        cliente.super_defi = 500
        cliente.pordia_grasa = 50
        cliente.pordia_proteina = 15 
        cliente.pordia_hc = 35

        funciones.MB(cliente)
        funciones.MB_FA(cliente)
        funciones.ET(cliente)
        funciones.GET(cliente)
        funciones.total_kcal(cliente)
        funciones.macronutrientes_diario(cliente)
        funciones.gramospeso(cliente)
        funciones.distribucion(cliente)
        
        rango = len(cliente.distribucion)
        return render_template("requerimientos.html", cliente=cliente,rango=rango)

@app.route("/registro_cliente/requerimientos/actualizados", methods=["POST"])
# En el caso de que el dietista no esté de acuerdo con los datos de los requerimientos, podrá editarlo
def actualizarRequerimientos():
    global cliente

    if request.method == "POST": 
        cliente.super_defi = int(request.form['superavit'])
        grasa = int(request.form['porcentaje_grasas'])
        proteina = int(request.form['porcentaje_proteinas'])
        hc = int(request.form['porcentaje_hc'])

        funciones.actualizarMacroDiarios(cliente,grasa,hc,proteina)
        funciones.MB(cliente)
        funciones.MB_FA(cliente)
        funciones.ET(cliente)
        funciones.GET(cliente)
        funciones.total_kcal(cliente)
        funciones.macronutrientes_diario(cliente)
        funciones.gramospeso(cliente)
        funciones.distribuciondiamacronutri(cliente)

        return render_template("requerimientos.html", cliente=cliente)

@app.route("/registro_cliente/cliente_registrado")
def ClienteRegistrado():
    global cliente
    funciones.agregarcliente(cliente)
    return render_template("confirmacion_cliente_registrado.html")

    
#--------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)