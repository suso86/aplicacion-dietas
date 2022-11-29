from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from werkzeug.utils import secure_filename
from os import remove
from datetime import timedelta

from cliente import Cliente

#hola
app=Flask(__name__)

i = 0
#Variable para recoger los datos mientras se registra un cliente
cliente = Cliente()

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        cliente.kcal = request.form['kcal']
        print(cliente.nombre, " ", cliente.sn_cliente_enfermedad, " ", cliente.verdura_fruta, " ", 
        cliente.actividad, " ", cliente.altura, " ", cliente.kcal)
    return render_template("base.html")

#-------------------------------------------------------------------------------------#
#Parte de la entrevista 
@app.route("/registro_cliente")
def Entrevista():
    global i
    i = i + 1
    print(i)
    return render_template("datos_basicos.html")

@app.route("/registro_cliente/antecedentes", methods=["POST"])
def SaludAntecedentes():
    global i
    global cliente
    i = i + 1
    print(i)
    if request.method == "POST":
        cliente.nombre = request.form['nombre_cliente']
        nombre_cliente = request.form['nombre_cliente']
        primer_apellido = request.form['primer_apellido']
        segundo_apellido = request.form['segundo_apellido']
        direccion_cliente = request.form['direccion_cliente']
        edad_cliente = request.form['edad_cliente']
        hm_cliente = request.form['hm_cliente']
        numero_tlf = request.form['numero_tlf']

        print(cliente.nombre, " ", cliente.sn_cliente_enfermedad, " ", cliente.verdura_fruta, " ", 
        cliente.actividad, " ", cliente.altura, " ", cliente.kcal)

        return render_template("datos_clinicos.html", nombre_cliente=nombre_cliente, primer_apellido=primer_apellido,
        segundo_apellido=segundo_apellido,direccion_cliente=direccion_cliente,edad_cliente=edad_cliente,hm_cliente=hm_cliente,
        numero_tlf=numero_tlf)

@app.route("/registro_cliente/habitos", methods=["POST"])
def HabitosAlimenticios():
    global i
    global cliente
    i =i + 1
    print(i)
    if request.method == "POST":
        cliente.sn_cliente_enfermedad = request.form['sn_cliente_enfermedad']
        nombre_cliente = request.form['nombre_cliente']
        primer_apellido = request.form['primer_apellido']
        segundo_apellido = request.form['segundo_apellido']
        direccion_cliente = request.form['direccion_cliente']
        edad_cliente = request.form['edad_cliente']
        hm_cliente = request.form['hm_cliente']
        numero_tlf = request.form['numero_tlf']
        sn_cliente_enfermedad = request.form['sn_cliente_enfermedad']
        cual_enfermedad = request.form['cual_enfermedad']
        sn_cliente_alergia = request.form['sn_cliente_alergia']
        cual_alergia = request.form['cual_alergia']
        sn_cliente_antecedentes = request.form['sn_cliente_antecedentes']
        cual_antecedentes = request.form['cual_antecedentes']
        
        print(cliente.nombre, " ", cliente.sn_cliente_enfermedad, " ", cliente.verdura_fruta, " ", 
        cliente.actividad, " ", cliente.altura, " ", cliente.kcal)
        
        return render_template("habitos_alimenticios.html", nombre_cliente=nombre_cliente, primer_apellido=primer_apellido,
        segundo_apellido=segundo_apellido,direccion_cliente=direccion_cliente,edad_cliente=edad_cliente,hm_cliente=hm_cliente,
        numero_tlf=numero_tlf,sn_cliente_enfermedad=sn_cliente_enfermedad, cual_enfermedad=cual_enfermedad,
        sn_cliente_alergia=sn_cliente_alergia,cual_alergia=cual_alergia, sn_cliente_antecedentes=sn_cliente_antecedentes,
        cual_antecedentes=cual_antecedentes)

@app.route("/registro_cliente/estilo", methods=["POST"])
def EstiloVida():
    global i
    global cliente
    i = i + 1
    print(i)
    if request.method == "POST":
        cliente.verdura_fruta = request.form['verdura_fruta']
        """
        nombre_cliente = request.form['nombre_cliente']
        primer_apellido = request.form['primer_apellido']
        segundo_apellido = request.form['segundo_apellido']
        direccion_cliente = request.form['direccion_cliente']
        edad_cliente = request.form['edad_cliente']
        hm_cliente = request.form['hm_cliente']
        numero_tlf = request.form['numero_tlf']
        sn_cliente_enfermedad = request.form['sn_cliente_enfermedad']
        cual_enfermedad = request.form['cual_enfermedad']
        sn_cliente_alergia = request.form['sn_cliente_alergia']
        cual_alergia = request.form['cual_alergia']
        sn_cliente_antecedentes = request.form['sn_cliente_antecedentes']
        cual_antecedentes = request.form['cual_antecedentes']
        verdura_fruta = request.form['verdura_fruta']
        legumbres_cereales = request.form['legumbres_cereales']
        pescado_carne = request.form['pescado_carne']
        frutos_secos = request.form['frutos_secos']
        lacteos = request.form['lacteos']
        aceite = request.form['aceite']
        preparar_alimentos = request.form['preparar_alimentos']
        historial = request.form['historial']
        edad_maxima = request.form['edad_maxima']
        causa = request.form['causa']
        sn_cliente_regimen = request.form['sn_cliente_regimen']
        cual_regimen_nutricional = request.form['cual_regimen_nutricional']
        
        return render_template("estilo_vida.html", nombre_cliente=nombre_cliente, primer_apellido=primer_apellido,
        segundo_apellido=segundo_apellido,direccion_cliente=direccion_cliente,edad_cliente=edad_cliente,hm_cliente=hm_cliente,
        numero_tlf=numero_tlf,sn_cliente_enfermedad=sn_cliente_enfermedad, cual_enfermedad=cual_enfermedad,
        sn_cliente_alergia=sn_cliente_alergia,cual_alergia=cual_alergia, sn_cliente_antecedentes=sn_cliente_antecedentes,
        cual_antecedentes=cual_antecedentes,verdura_fruta=verdura_fruta,legumbres_cereales=legumbres_cereales,
        pescado_carne=pescado_carne, frutos_secos=frutos_secos, lacteos=lacteos, aceite=aceite, preparar_alimentos=preparar_alimentos,
        historial=historial, edad_maxima=edad_maxima, causa=causa, sn_cliente_regimen=sn_cliente_regimen, cual_regimen_nutricional=cual_regimen_nutricional)
        """
        print(cliente.nombre, " ", cliente.sn_cliente_enfermedad, " ", cliente.verdura_fruta, " ", 
        cliente.actividad, " ", cliente.altura, " ", cliente.kcal)
        return render_template("estilo_vida.html")

@app.route("/registro_cliente/evaluacion", methods=["POST"])
def EvaluacionAntropometrica():
    global cliente
    if request.method == "POST":
        cliente.actividad = request.form['actividad']
        print(cliente.nombre, " ", cliente.sn_cliente_enfermedad, " ", cliente.verdura_fruta, " ", 
        cliente.actividad, " ", cliente.altura, " ", cliente.kcal)
        return render_template("evaluacion_antropometrica.html")

@app.route("/registro_cliente/requerimientos", methods=["POST"])
def Requerimientos():
    global cliente
    if request.method == "POST":
        cliente.altura = request.form['altura']
        print(cliente.nombre, " ", cliente.sn_cliente_enfermedad, " ", cliente.verdura_fruta, " ", 
        cliente.actividad, " ", cliente.altura, " ", cliente.kcal)
        return render_template("requerimientos.html")


#--------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run(debug=True)