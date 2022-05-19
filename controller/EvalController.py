class EvaluadorController:
    def __init__(self) -> None:
        super().__init__()
        # FIXME convertirlo en diccionario cuya llave sea el id del estudiante y el valor una lista de las evaluaciones que se han hecho para el mismo estudiante
        self.evaluaciones = []
        self.nombres = {}
        self.calificaciones = {}
        self.criterios = {"Actuales": {"Desarrollo y profundidad en el tratamiento del tema": 20,
                                       "Desafío académico y científico del tema": 15,
                                       "Cumplimiento de los objetivos propuestos": 10,
                                       "Creatividad e innovación de las soluciones y desarrollos propuestos": 10,
                                       "Validez de los resultados y conclusiones": 20,
                                       "Manejo y procesamiento de la información y bibliografía": 10,
                                       "Calidad y presentación del documento escrito": 7.5,
                                       "Presentación oral": 7.5} }
    #a
    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)
