from cliente import Cliente


def MB(cliente): #Metabolismo Basal
    
    if cliente.sexo== 'Hombre':
        cliente.MB= 10* cliente.peso +6.25 * cliente.altura- 5 *cliente.edad+5
    elif cliente.sexo=='Mujer':
        cliente.MB= 10* cliente.peso +6.25 * cliente.altura- 5 *cliente.edad-161
    return cliente.MB

def MB_FA(cliente): #Metabolismo Basal no se que
    
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
    return cliente.MB_FA


def ET(cliente): # ni puta idea que es
    if cliente.proteinas> 0.25:
        cliente.ET= 0.12* cliente.MB
    else:
        cliente.ET=0.10*cliente.MB
    return cliente.ET


def GET(cliente):
    cliente.GET= cliente.ET+ cliente.MB_FA
    