import streamlit as st

def calificar_acta(st, controller):
    ids = []
    nombres = controller.nombres
    st.title("CALIFICACIÓN DE ACTAS ")
    st.subheader("Selecciona el ID del estudiante a calificar")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
    if (seleccion != None):
        st.text("Estás calificando a "+str(nombres.get(seleccion)))
        st.subheader("Criterios a calificar")
        criterio_1 = st.number_input("Desarrollo y profundidad en el tratamiento del tema:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_1 = st.text_input("Observaciones:")
        criterio_2 = st.number_input("Desafío académico y científico del tema:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_2 = st.text_input("Observaciones: ")
        criterio_3 = st.number_input("Cumplimiento de los objetivos propuestos:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_3 = st.text_input("Observaciones:  ")
        criterio_4 = st.number_input("Creatividad e innovación de las soluciones y desarrollos propuestos:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_4 = st.text_input("Observaciones:   ")
        criterio_5 = st.number_input("Validez de los resultados y conclusiones:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_5 = st.text_input("Observaciones:    ")
        criterio_6 = st.number_input("Manejo y procesamiento de la información y bibliografía:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_6 = st.text_input("Observaciones:     ")
        criterio_7 = st.number_input("Calidad y presentación del documento escrito:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_7 = st.text_input("Observaciones:      ")
        guardar = st.button("Guardar")
        if guardar:
            notas = []
            t_1 = (criterio_1, observacion_1)
            notas.append(t_1)
            t_2 = (criterio_2, observacion_2)
            notas.append(t_2)
            t_3 = (criterio_3, observacion_3)
            notas.append(t_3)
            t_4 = (criterio_4, observacion_4)
            notas.append(t_4)
            t_5 = (criterio_5, observacion_5)
            notas.append(t_5)
            t_6 = (criterio_6, observacion_6)
            notas.append(t_6)
            t_7 = (criterio_7, observacion_7)
            notas.append(t_7)
            controller.calificaciones[seleccion] = notas