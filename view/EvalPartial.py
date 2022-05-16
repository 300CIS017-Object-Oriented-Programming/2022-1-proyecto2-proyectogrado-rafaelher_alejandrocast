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
    evaluacion_obj.jurado1 = st.text_input("Jurado 1")
    evaluacion_obj.jurado2 = st.text_input("Jurado 2")


    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Guardar")

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


            st.header("Nombre")
            st.write(evaluacion.id_estudiante)
       # with col1:
            st.header("id estudiante")
            st.write(evaluacion.nombre)
        #with col1:
            st.header("Tema proyecto")
            st.write(evaluacion.tema_proyecto)
        #with col1:
            st.header("Periodo")
            st.write(evaluacion.periodo)
        #with col1:
            st.header("Director")
            st.write(evaluacion.director)
        #with col1:
            st.header("Co-director")
            st.write(evaluacion.co_director)
        #with col1:
            st.header("Enfasis")
            st.write(evaluacion.enfasis)
        #with col1:
            st.header("Modalidad")
            st.write(evaluacion.modalidad)
        #with col1:
            st.header("Jurado 1")
            st.write(evaluacion.jurado1)
        #with col1:
            st.header("Jurado 2")
            st.write(evaluacion.jurado2)

