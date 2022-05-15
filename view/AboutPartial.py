from model.EvalAnteproy import EvaluacionAnteproyecto

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    evaluacion_obj2 = EvaluacionAnteproyecto()
    evaluacion_obj2.nombre = st.text_input("Nombre estudiante")
    evaluacion_obj2.id_estudiante = st.text_input("Id estudiante")
    evaluacion_obj2.tema_proyecto = st.text_input("Tema proyecto")
    option = st.selectbox(
        'como te podemos contactar?',
        ('Email', 'telefono fijo', 'telefono celular'))

    st.write('has seleccionado:', option)
    evaluacion_obj2.id_metodocontacto = st.text_input("Metodo contacto")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Submit")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj2)
        st.write("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def listar_evaluacion2(st, controller):
    """Itera los elementos de evaluacion agregados y los muestra"""
    st.title("Datos guardados")
    for evaluacion in controller.evaluaciones:

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Nombre")
            st.write(evaluacion.id_estudiante2)

        with col2:
            st.header("id estudiante")
            st.write(evaluacion.nombre2)

        with col3:
            st.header("Tema proyecto")
            st.write(evaluacion.tema_proyecto2)

        with col4:
            st.header("Contacto")
            st.write(evaluacion.id_metodocontacto2)
