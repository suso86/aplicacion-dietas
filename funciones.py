from cliente import Cliente


def MB(cliente): #Metabolismo Basal
    if cliente.sexo== 'Hombre':
        cliente.MB= 10* cliente.peso +6.25 * cliente.altura- 5 *cliente.edad+5
    elif cliente.sexo=='Mujer':
        cliente.MB= 10* cliente.peso +6.25 * cliente.altura- 5 *cliente.edad-161


def MB_FA(cliente): #Metabolismo Basal por Frecuencia de Actividad
    if cliente.actividad=='Muy ligera':
        cliente.MB_FA=cliente.MB*1.2
    elif cliente.actividad=='Ligera':
        cliente.MB_FA=cliente.MB*1.375
    elif cliente.actividad=='Moderada':
        cliente.MB_FA=cliente.MB*1.55
    elif cliente.actividad=='Alta':
        cliente.MB_FA=cliente.MB*1.725
    elif cliente.actividad=='Muy Alta':
        cliente.MB_FA=cliente.MB*1.9


def ET(cliente): #Efecto Termogénico
    if cliente.pordia_proteina> 0.25:
        cliente.ET= 0.12* cliente.MB
    else:
        cliente.ET=0.10*cliente.MB


def GET(cliente): #Gasto Energético Total
    cliente.GET= cliente.ET+ cliente.MB_FA


def total_kcal(cliente): #Total de kcal necesitadas según el motivo de la consulta
    if cliente.motivo_consulta== 'Mantenimiento de peso':
        cliente.kcal=cliente.GET
    elif cliente.motivo_consulta=='Pérdida de peso':
        cliente.kcal=cliente.GET - cliente.super_defi
    elif cliente.motivo_consulta=='Ganancia de peso':
        cliente.kcal=cliente.GET + cliente.super_defi


def macronutrientes_diario(cliente): #Porcentaje de grasa/prot/hc por kcal entre 9 o 4
    cliente.grasa= cliente.pordia_grasa*cliente.kcal/9
    cliente.proteina= cliente.pordia_proteina*cliente.kcal/4
    cliente.hc= cliente.pordia_hc*cliente.kcal/4


def gramospeso(cliente): #gramos macronutrientes en el peso
    cliente.gr_grasa=cliente.grasa/cliente.peso
    cliente.gr_proteina=cliente.proteina/cliente.peso
    cliente.gr_hc=cliente.hc/cliente.peso
