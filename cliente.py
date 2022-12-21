import numpy

class Cliente:
    def __init__(self):
        # datos básicos
        self.nombre=""
        self.primer_apellido=""
        self.segundo_apellido=""
        self.direccion=""
        self.edad=0
        self.sexo=""
        self.telefono=0

        # datos clínicos
        self.sn_cliente_enfermedad=""
        self.cual_enfermedad=""
        self.sn_cliente_alergia=""
        self.cual_alergia=""
        self.sn_cliente_antecedentes=""
        self.cual_antecedentes=""
        self.sn_cliente_estreñimiento=""
        self.cual_estreñimiento=""
        self.sn_cliente_hormonal=""
        self.cual_hormonal=""

        # hábitos alimenticios
        self.verdura_fruta=""
        self.legumbres_cereales=""
        self.pescado_carne=""
        self.frutos_secos=""
        self.lacteos=""
        self.aceite=""
        self.preparar_alimentos=""
        self.historial=""
        self.edad_maxima=0
        self.causa=""
        self.sn_cliente_regimen=""
        self.cual_regimen_nutricional=""

        # estilo de vida
        self.actividad=""
        self.sn_cliente_alcohol=""
        self.sn_cliente_cafe=""
        self.sn_cliente_tabaco=""
        self.sueño=0
        self.frecuencia_comida=""
        self.encargado_compra=""
        self.frecuencia_compras=""
        self.sn_gustar_cocinar=""
        self.mas_hambre=""
        self.desayuno_habitual=""
        self.merienda_habitual=""
        self.preferencia_merienda=""
        self.preferencia_desayuno=""
        self.platos=""
        self.comidas_realizar=[]

        #Evaluación antropometrica
        self.altura=0
        self.peso=0
        self.graso=0
        self.brazo=0
        self.cintura=0
        self.cuadriceps=0
        self.espalda=0
        self.hombro=0
        self.piernas=0

        #Requerimientos energeticos
        self.kcal=0
        self.proteinas=0
        self.grasas=0
        self.hc=0
        
        #De los Cálculos
        self.MB=0
        self.MB_FA=0
        self.GET=0
        self.ET=0

        # Porcentajes de macronutrientes diarios
        self.pordia_grasa=0
        self.pordia_proteina=0
        self.pordia_hc=0

        #gramos macronutrientes por peso
        self.gr_grasa=0
        self.gr_proteina=0
        self.gr_hc=0

        #Extra de entrevista
        self.motivo_consulta=""
        self.super_defi=0
        self.distribucion=[]
        
        self.desayuno=[]
        self.mediamanana=[]
        self.comida=[]
        self.merienda=[]
        self.cena=[]
        self.recena=[]
        self.porc_desayuno=0
        self.porc_mediamanana=0
        self.porc_comida=0
        self.porc_merienda=0
        self.porc_cena=0
        self.porc_recena=0



