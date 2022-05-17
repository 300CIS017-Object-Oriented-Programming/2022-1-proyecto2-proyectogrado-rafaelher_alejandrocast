#from multiapp import *

def calificar_acta(st, controller):
    st.title("CALIFICACIÓN DE ACTAS ")
    st.subheader("Nombre")
    for calificacion in controller.evaluaciones:
        st.button(calificacion.id_estudiante)