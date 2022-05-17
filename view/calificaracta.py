import streamlit as st

def calificar_acta(st, controller):
    ids = []
    st.title("CALIFICACIÓN DE ACTAS ")
    st.subheader("Selecciona el ID del estudiante a calificar")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
    st.text(seleccion)
    if(seleccion != '0'):
        criterio_1 = st.slider("Desarrollo y profundidad en el tratamiento del tema: ", min_value=0.0, max_value=5.0,
                               step=0.1)
