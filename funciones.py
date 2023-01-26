from cliente import Cliente

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


def agregarcliente():
    mydb=mysql.connector.connect(host='localhost',user='root',password='123456',
                                database='dietas')
    mycursor=mydb.cursor()
    mycursor.execute("INSERT INTO clientes VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (cliente.nombre,
        cliente.primer_apellido,
        cliente.segundo_apellido,
        cliente.direccion ,
        cliente.edad,
        cliente.sexo,
        cliente.telefono,
        cliente.altura,
        cliente.peso,
        cliente.brazo,
        cliente.cintura,
        cliente.cuadriceps,
        cliente.espalda,
       cliente.hombro,
        cliente.piernas,
        cliente.kcal,
        cliente.proteinas,
        cliente.grasas,
        cliente.hc,
        cliente.MB,
        cliente.MB_FA,
        cliente.GET,
       cliente.ET,
        cliente.sn_cliente_enfermedad,
        cliente.cual_enfermedad,
        cliente.sn_cliente_alergia,
        cliente.cual_alergia,
        cliente.sn_cliente_antecedentes,
        cliente.cual_antecedentes,
        cliente.sn_cliente_estreñimiento,
        cliente.cual_estreñimiento,
        cliente.sn_cliente_hormonal,
        cliente.cual_hormonal,
        cliente.verdura_fruta,
        cliente.legumbres_cereales,
        cliente.pescado_carne,
        cliente.frutos_secos,
        cliente.lacteos,
        cliente.aceite,
       cliente.preparar_alimentos ,
        cliente.historial,
        cliente.edad_maxima,
        cliente.causa,
        cliente.sn_cliente_regimen,
        cliente.cual_regimen_nutricional text,
        cliente.actividad,
        cliente.sn_cliente_alcohol,
        cliente.sn_cliente_cafe,
        cliente.sn_cliente_tabaco,
        cliente.sueño,
        cliente.frecuencia_comida,
        cliente.encargado_compra,
        cliente.frecuencia_compra,
        cliente.sn_gustar_cocinar,
        cliente.mas_hambre,
        cliente.desayuno_habitual,
        cliente.merienda_habitual,
        cliente.preferencia_merienda,
       cliente.preferencia_desayuno,
       cliente.platos,
        cliente.comidas_realizar,
        cliente.motivo_consulta,
        cliente.super_defi ,
       cliente.pordia_grasa,
        cliente.pordia_proteina ,
        cliente.pordia_hc ,
        cliente.gr_grasa ,
        cliente.gr_proteina ,
        cliente.gr_hc ,
        cliente.desayuno_diario,
        cliente.mediamanana_diario,
        cliente.comida_diario,
        cliente.merienda_diario,
        cliente.cena_diario,
        cliente.recena_diario,
        cliente.porc_comidas))
    mydb.commit()
    mydb.close()