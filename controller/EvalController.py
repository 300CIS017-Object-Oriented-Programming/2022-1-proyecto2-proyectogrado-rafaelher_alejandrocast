class EvaluadorController:
    def __init__(self) -> None:
        super().__init__()
        # FIXME convertirlo en diccionario cuya llave sea el id del estudiante y el valor una lista de las evaluaciones que se han hecho para el mismo estudiante
        self.evaluaciones = []

    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)

    def agregar_evaluacion2(self, evaluacion2_obj):
        self.evaluaciones2.append(evaluacion2_obj)


