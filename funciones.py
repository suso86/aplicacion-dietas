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
        cliente.kcal=cliente.GET - cliente.super_defi
    elif cliente.motivo_consulta =='ganancia de peso':
        cliente.kcal=cliente.GET + cliente.super_defi
    
    cliente.kcal=round(cliente.kcal,2)


def macronutrientes_diario(cliente): #Porcentaje de grasa/prot/hc por kcal entre 9 o 4
    cliente.grasas= round(cliente.pordia_grasa*cliente.kcal/9,2)
    cliente.proteinas= round(cliente.pordia_proteina*cliente.kcal/4,2)
    cliente.hc= round(cliente.pordia_hc*cliente.kcal/4,2)

def gramospeso(cliente): #gramos macronutrientes en el peso
    cliente.gr_grasa=round(cliente.grasas/int(cliente.peso),2)
    cliente.gr_proteina=round(cliente.proteinas/int(cliente.peso),2)
    cliente.gr_hc=round(cliente.hc/int(cliente.peso),2)


def distribuciondiamacronutri(cliente): #Distribución por comida de los macronutrientes
    
    cliente.desayuno=["desayuno",cliente.kcal*cliente.porc_desayuno,
                        cliente.grasas*cliente.porc_desayuno,
                        cliente.proteinas*cliente.porc_desayuno,
                        cliente.hc*cliente.porc_desayuno]

    cliente.mediamanana=["media-mañana",cliente.kcal*cliente.porc_mediamanana,
                    cliente.grasas*cliente.porc_mediamanana,
                    cliente.proteinas*cliente.porc_mediamanana,
                    cliente.hc*cliente.porc_mediamanana]
                                            
    
    cliente.comida=["almuerzo",cliente.kcal*cliente.porc_comida,
                cliente.grasas*cliente.porc_comida,
                cliente.proteinas*cliente.porc_comida,
                cliente.hc*cliente.porc_comida]

    cliente.merienda=["merienda",cliente.kcal*cliente.porc_merienda,
                    cliente.grasas*cliente.porc_merienda,
                    cliente.proteinas*cliente.porc_merienda,
                    cliente.hc*cliente.porc_merienda]
    
    cliente.cena=["cena",cliente.kcal*cliente.porc_cena,
                cliente.grasas*cliente.porc_cena,
                cliente.proteinas*cliente.porc_cena,
                cliente.hc*cliente.porc_cena]

    cliente.recena=["recena",cliente.kcal*cliente.porc_recena,
                cliente.grasas*cliente.porc_recena,
                cliente.proteinas*cliente.porc_recena,
                cliente.hc*cliente.porc_recena]

def distribucion(cliente):
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