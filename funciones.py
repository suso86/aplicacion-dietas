from cliente import Cliente
import mysql.connector

"""
Acordarnos de cambiar los valores fijos por valores dependiendo del nutricionista:
super_defi = 500
pordia_grasas = 50
pordia_proteina = 15
pordia_hc = 35
"""

def MB(cliente): #Metabolismo Basal
    if cliente.sexo== 'hombre':
        cliente.MB= 10* int(cliente.peso) + 6.25 * int(cliente.altura) - 5 *int(cliente.edad)+5
    elif cliente.sexo=='mujer':
        cliente.MB= 10* int(cliente.peso) + 6.25 * int(cliente.altura) - 5 *int(cliente.edad)-161

    cliente.MB=round(cliente.MB,2)

def MB_FA(cliente): #Metabolismo Basal por Frecuencia de Actividad
    if cliente.actividad=='muy ligera':
        cliente.MB_FA=cliente.MB*1.2
    elif cliente.actividad=='ligera':
        cliente.MB_FA=cliente.MB*1.375
    elif cliente.actividad=='moderada':
        cliente.MB_FA=cliente.MB*1.55
    elif cliente.actividad=='alta':
        cliente.MB_FA=cliente.MB*1.725
    elif cliente.actividad=='muy alta':
        cliente.MB_FA=cliente.MB*1.9
    
    cliente.MB_FA=round(cliente.MB_FA,2)


def ET(cliente): #Efecto Termogénico
    if cliente.pordia_proteina > 25:
        cliente.ET= 0.12* cliente.MB
    else:
        cliente.ET=0.10*cliente.MB

    cliente.ET=round(cliente.ET,2)

def GET(cliente): #Gasto Energético Total
    cliente.GET= cliente.ET+ cliente.MB_FA
    cliente.GET= round(cliente.GET,2)


def total_kcal(cliente): #Total de kcal necesitadas según el motivo de la consulta
    if cliente.motivo_consulta == 'mantenimiento de peso':
        cliente.kcal=cliente.GET
    elif cliente.motivo_consulta =='perdida de peso':
        cliente.kcal=int(cliente.GET) - int(cliente.super_defi)
    elif cliente.motivo_consulta =='ganancia de peso':
        cliente.kcal=int(cliente.GET) + int(cliente.super_defi)
    
    cliente.kcal=round(cliente.kcal,2)


def macronutrientes_diario(cliente): #Porcentaje de grasa/prot/hc por kcal entre 9 o 4
    cliente.grasas= round((cliente.pordia_grasa/100)*cliente.kcal/9,2)
    cliente.proteinas= round((cliente.pordia_proteina/100)*cliente.kcal/4,2)
    cliente.hc= round((cliente.pordia_hc/100)*cliente.kcal/4,2)

def gramospeso(cliente): #gramos macronutrientes en el peso
    cliente.gr_grasa=round(cliente.grasas/int(cliente.peso),2)
    cliente.gr_proteina=round(cliente.proteinas/int(cliente.peso),2)
    cliente.gr_hc=round(cliente.hc/int(cliente.peso),2)


def distribuciondiamacronutri(cliente): #Distribución por comida de los macronutrientes
    # 0 --> kcal, 1 --> proteinas, 2 --> grasas, 3 --> hc
    cliente.desayuno=["desayuno",int(cliente.kcal*(cliente.desayuno_diario[0]/100)),
                        int(cliente.grasas*(cliente.desayuno_diario[2]/100)),
                        int(cliente.proteinas*(cliente.desayuno_diario[1]/100)),
                        int(cliente.hc*(cliente.desayuno_diario[3]/100)),cliente.desayuno_diario]

    cliente.mediamanana=["media-mañana",int(cliente.kcal*(cliente.mediamanana_diario[0]/100)),
                    int(cliente.grasas*(cliente.mediamanana_diario[2]/100)),
                    int(cliente.proteinas*(cliente.mediamanana_diario[1]/100)),
                    int(cliente.hc*(cliente.mediamanana_diario[3]/100)),cliente.mediamanana_diario]
                                            
    
    cliente.comida=["almuerzo",int(cliente.kcal*(cliente.comida_diario[0]/100)),
                int(cliente.grasas*(cliente.comida_diario[2]/100)),
                int(cliente.proteinas*(cliente.comida_diario[1]/100)),
                int(cliente.hc*(cliente.comida_diario[3]/100)),cliente.comida_diario]

    cliente.merienda=["merienda",int(cliente.kcal*(cliente.merienda_diario[0]/100)),
                    int(cliente.grasas*(cliente.merienda_diario[2]/100)),
                    int(cliente.proteinas*(cliente.merienda_diario[1]/100)),
                    int(cliente.hc*(cliente.merienda_diario[3]/100)),cliente.merienda_diario]
    
    cliente.cena=["cena",int(cliente.kcal*(cliente.cena_diario[0]/100)),
                int(cliente.grasas*(cliente.cena_diario[2]/100)),
                int(cliente.proteinas*(cliente.cena_diario[1]/100)),
                int(cliente.hc*(cliente.cena_diario[3]/100)),cliente.cena_diario]

    cliente.recena=["recena",int(cliente.kcal*(cliente.recena_diario[0]/100)),
                int(cliente.grasas*(cliente.recena_diario[2]/100)),
                int(cliente.proteinas*(cliente.recena_diario[1]/100)),
                int(cliente.hc*(cliente.recena_diario[3]/100)),cliente.recena_diario]

def distribucion(cliente):
    porcentajesdiarios(cliente)
    distribuciondiamacronutri(cliente)

    for comida in cliente.comidas_realizar:
        if comida == 'desayuno':
            cliente.distribucion.append(cliente.desayuno)
        elif comida == 'media-mañana':
            cliente.distribucion.append(cliente.mediamanana)
        elif comida == 'almuerzo':
            cliente.distribucion.append(cliente.comida)
        elif comida == 'merienda':
            cliente.distribucion.append(cliente.merienda)
        elif comida == 'cena':
            cliente.distribucion.append(cliente.cena)
    
        
        
        

def actualizarMacroDiarios(cliente,grasa,hc,proteina):
    #Primero comprobamos si no han variado
    if cliente.pordia_proteina == proteina and cliente.pordia_grasa == grasa and cliente.pordia_hc == hc:
        cliente.pordia_proteina = proteina
        cliente.pordia_grasa = grasa
        cliente.pordia_hc = hc

    #Primero comprobamo si los tres pocentajes han variado
    elif cliente.pordia_proteina != proteina and cliente.pordia_grasa != grasa and cliente.pordia_hc != hc:
        print("3/3")
        suma_macro = proteina + grasa + hc
        if suma_macro != 100:
            cliente.pordia_proteina = 50
            cliente.pordia_grasa = 15
            cliente.pordia_hc = 35
        else:
            cliente.pordia_proteina = proteina
            cliente.pordia_grasa = grasa
            cliente.pordia_hc = hc
    
    #Después comprobamos si 2/3 porcentajes han variado
    elif cliente.pordia_proteina == proteina and cliente.pordia_grasa != grasa and cliente.pordia_hc != hc:
        print("2/3")
        cliente.pordia_proteina = 100 - (grasa+hc)
        cliente.pordia_grasa = grasa
        cliente.pordia_hc = hc 
    
    elif cliente.pordia_proteina != proteina and cliente.pordia_grasa == grasa and cliente.pordia_hc != hc:
        print("2/3")
        cliente.pordia_proteina = proteina
        cliente.pordia_grasa = 100 - (proteina+hc)
        cliente.pordia_hc = hc

    elif cliente.pordia_proteina != proteina and cliente.pordia_grasa != grasa and cliente.pordia_hc == hc:
        print("2/3")
        cliente.pordia_proteina = proteina
        cliente.pordia_grasa = grasa
        cliente.pordia_hc = 100 - (proteina+grasa)

    #Por último comprobamos si 1/3 porcentajes ha variado
    else:
        print("1/3")
        if cliente.pordia_proteina != proteina:
            print("proteina")
            cliente.pordia_grasa = 100-(proteina+cliente.pordia_hc)
            cliente.pordia_proteina = proteina
        elif cliente.pordia_grasa != grasa:
            print("grasa")
            cliente.pordia_hc = 100-(grasa+cliente.pordia_proteina)
            cliente.pordia_grasa = grasa
        elif cliente.pordia_hc != hc:
            print("hc")
            cliente.pordia_proteina = 100 - (hc+cliente.pordia_grasa)
            cliente.pordia_hc = hc

def porcentajesdiarios(cliente):
    n_comidas = len(cliente.comidas_realizar)
    if n_comidas == 6:
        for i in range(4):
            cliente.desayuno_diario.append(20)
            cliente.mediamanana_diario.append(15)
            cliente.comida_diario.append(25)
            cliente.merienda_diario.append(15)
            cliente.cena_diario.append(25)
            cliente.recena_diario.append(0)
    
    elif n_comidas == 5:
        aux = int(100/5)
        for i in range(4):
            cliente.desayuno_diario.append(aux)
            cliente.mediamanana_diario.append(aux)
            cliente.comida_diario.append(aux)
            cliente.merienda_diario.append(aux)
            cliente.cena_diario.append(aux)
            cliente.recena_diario.append(aux)

    elif n_comidas == 4:
        aux = int(100/4)
        for i in range(4):
            cliente.desayuno_diario.append(aux)
            cliente.mediamanana_diario.append(aux)
            cliente.comida_diario.append(aux)
            cliente.merienda_diario.append(aux)
            cliente.cena_diario.append(aux)
            cliente.recena_diario.append(aux)

    elif n_comidas == 3:
        aux = int(100/3)
        for i in range(4):
            cliente.desayuno_diario.append(aux)
            cliente.mediamanana_diario.append(aux)
            cliente.comida_diario.append(aux)
            cliente.merienda_diario.append(aux)
            cliente.cena_diario.append(aux)
            cliente.recena_diario.append(aux)

    elif n_comidas == 2:
        aux = int(100/2)
        for i in range(4):
            cliente.desayuno_diario.append(aux)
            cliente.mediamanana_diario.append(aux)
            cliente.comida_diario.append(aux)
            cliente.merienda_diario.append(aux)
            cliente.cena_diario.append(aux)
            cliente.recena_diario.append(aux)

    elif n_comidas == 1:
        aux = int(100/1)
        for i in range(4):
            cliente.desayuno_diario.append(aux)
            cliente.mediamanana_diario.append(aux)
            cliente.comida_diario.append(aux)
            cliente.merienda_diario.append(aux)
            cliente.cena_diario.append(aux)
            cliente.recena_diario.append(aux)

def agregarcliente(cliente):
    mydb=mysql.connector.connect(host='localhost',user='root',password='123456',
                                database='dietas')
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO clientes VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (str(cliente.nombre),
        str(cliente.primer_apellido),
        str(cliente.segundo_apellido),
        str(cliente.direccion ),
        str(cliente.edad),
        str(cliente.sexo),
        str(cliente.telefono),
        str(cliente.altura),
        str(cliente.peso),
        str(cliente.brazo),
        str(cliente.cintura),
        str(cliente.cuadriceps),
        str(cliente.espalda),
       str(cliente.hombro),
        str(cliente.piernas),
        str(cliente.kcal),
        str(cliente.proteinas),
        str(cliente.grasas),
        str(cliente.hc),
        str(cliente.MB),
        str(cliente.MB_FA),
        str(cliente.GET),
       str(cliente.ET),
        str(cliente.sn_cliente_enfermedad),
        str(cliente.cual_enfermedad),
        str(cliente.sn_cliente_alergia),
        str(cliente.cual_alergia),
        str(cliente.sn_cliente_antecedentes),
        str(cliente.cual_antecedentes),
        str(cliente.sn_cliente_estreñimiento),
        str(cliente.cual_estreñimiento),
        str(cliente.sn_cliente_hormonal),
        str(cliente.cual_hormonal),
        str(cliente.verdura_fruta),
        str(cliente.legumbres_cereales),
        str(cliente.pescado_carne),
        str(cliente.frutos_secos),
        str(cliente.lacteos),
        str(cliente.aceite),
       str(cliente.preparar_alimentos) ,
        str(cliente.historial),
        str(cliente.edad_maxima),
        str(cliente.causa),
        str(cliente.sn_cliente_regimen),
        str(cliente.cual_regimen_nutricional),
        str(cliente.actividad),
        str(cliente.sn_cliente_alcohol),
        str(cliente.sn_cliente_cafe),
        str(cliente.sn_cliente_tabaco),
        str(cliente.sueño),
        str(cliente.frecuencia_comida),
        str(cliente.encargado_compra),
        str(cliente.frecuencia_compras),
        str(cliente.sn_gustar_cocinar),
        str(cliente.mas_hambre),
        str(cliente.desayuno_habitual),
        str(cliente.merienda_habitual),
        str(cliente.preferencia_merienda),
       str(cliente.preferencia_desayuno),
       str(cliente.platos),
        ##cliente.comidas_realizar,
        str(cliente.motivo_consulta),
        str(cliente.super_defi ),
       str(cliente.pordia_grasa),
        str(cliente.pordia_proteina ),
        str(cliente.pordia_hc ),
        str(cliente.gr_grasa ),
        str(cliente.gr_proteina) ,
        str(cliente.gr_hc) ,
        ##cliente.desayuno_diario,
        ##cliente.mediamanana_diario,
        ##cliente.comida_diario,
        ##cliente.merienda_diario,
        ##cliente.cena_diario,
        ##cliente.recena_diario,
        ##cliente.porc_comidas)
        ))
    mydb.commit()
    mydb.close()