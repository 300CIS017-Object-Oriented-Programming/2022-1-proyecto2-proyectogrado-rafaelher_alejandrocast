import streamlit as st

def calificar_acta(st, controller):
    ids = []
    st.title("CALIFICACIÓN DE ACTAS ")
    st.subheader("Selecciona el ID del estudiante a calificar")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
    st.subheader("Criterios a calificar")
    if(seleccion != '0'):
        criterio_1 = st.slider("Desarrollo y profundidad en el tratamiento del tema:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_1 = st.text_input("Observaciones:")
        criterio_2 = st.slider("Desafío académico y científico del tema:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_2 = st.text_input("Observaciones: ")
        criterio_3 = st.slider("Cumplimiento de los objetivos propuestos:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_3 = st.text_input("Observaciones:  ")
        criterio_4 = st.slider("Creatividad e innovación de las soluciones y desarrollos propuestos:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_4 = st.text_input("Observaciones:   ")
        criterio_5 = st.slider("Validez de los resultados y conclusiones:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_5 = st.text_input("Observaciones:    ")
        criterio_6 = st.slider("Manejo y procesamiento de la información y bibliografía:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_6 = st.text_input("Observaciones:     ")
        criterio_7 = st.slider("Calidad y presentación del documento escrito:",min_value=0.0, max_value=5.0, step=0.1)
        observacion_7 = st.text_input("Observaciones:      ")