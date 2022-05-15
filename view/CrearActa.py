from model.EvalAnteproy import EvaluacionAnteproyecto

def agregar_evaluacion2(st, controller):
    # Objecto que modelará el formulario
    evaluacion2_obj = EvaluacionAnteproyecto()
    evaluacion2_obj.nombre = st.text_input("Nombre estudiante")
    evaluacion2_obj.id_estudiante = st.text_input("Id estudiante")
    evaluacion2_obj.tema_proyecto = st.text_input("Tema proyecto")
    option = st.selectbox(
        'como te podemos contactar?',
        ('Email', 'telefono fijo', 'telefono celular'))

    st.write('has seleccionado:', option)
    evaluacion2_obj.id_metodocontacto = st.text_input("Metodo contacto")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Submit")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion(evaluacion2_obj)
        st.write("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal

    return controller





def agregar_acta(st, controller):
    # Objecto que modelará el formulario
    evaluacion2_obj = EvaluacionAnteproyecto()
    evaluacion2_obj.nombre = st.text_input("Nombre estudiante")
    evaluacion2_obj.id_estudiante = st.text_input("Id estudiante")
    evaluacion2_obj.tema_proyecto = st.text_input("Tema proyecto")
    option = st.selectbox(
        'como te podemos contactar?',
        ('Email', 'telefono fijo', 'telefono celular'))

    st.write('has seleccionado:', option)
    evaluacion2_obj.id_metodocontacto = st.text_input("Metodo contacto")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Submit")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion2(evaluacion2_obj)
        st.write("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller



def listar_actas(st, controller):
    """Itera los elementos de evaluacion agregados y los muestra"""
    st.title("Datos guardados")
    for evaluacion2 in controller.evaluaciones2:

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Nombre")
            st.write(evaluacion2.id_estudiante)

        with col2:
            st.header("id estudiante")
            st.write(evaluacion2.nombre)

        with col3:
            st.header("Tema proyecto")
            st.write(evaluacion2.tema_proyecto)

        with col4:
            st.header("Contacto")
            st.write(evaluacion2.id_metodocontacto)








