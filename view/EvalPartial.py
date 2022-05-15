from model.EvalAnteproy import EvaluacionAnteproyecto

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def instrucciones():
    return """
           #### ¡bienvenido!
           Por favor rellenar todos los espacios en este apartado para poder crear el acta. \n\n\n\n\n

           """

def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Autor Trabajo de grado")
    evaluacion_obj.id_estudiante = st.text_input("Id estudiante")
    evaluacion_obj.tema_proyecto = st.text_input("Tema proyecto")
    evaluacion_obj.periodo = st.text_input("Periodo")
    evaluacion_obj.director = st.text_input("Director")
    evaluacion_obj.co_director = st.text_input("Co-Director")
    evaluacion_obj.enfasis = st.text_input("Enfasis")
    evaluacion_obj.modalidad = st.text_input("Modalidad")
    evaluacion_obj.Jurado1 = st.text_input("Jurado 1")
    evaluacion_obj.Jurado2 = st.text_input("Jurado 2")


    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Submit")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj)
        st.write("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def listar_evaluacion(st, controller):
    """Itera los elementos de evaluacion agregados y los muestra"""
    st.title("Datos guardados")
    for evaluacion in controller.evaluaciones:

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Nombre")
            st.write(evaluacion.id_estudiante)

        with col2:
            st.header("id estudiante")
            st.write(evaluacion.nombre)

        with col3:
            st.header("Tema proyecto")
            st.write(evaluacion.tema_proyecto)

        with col4:
            st.header("Contacto")
            st.write(evaluacion.id_metodocontacto)

