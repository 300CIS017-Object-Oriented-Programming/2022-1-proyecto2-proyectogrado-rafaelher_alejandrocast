import streamlit as st
def search(index, d):
   i = 0
   for key in d:
      if i == index:
         return key
      i+=1

def calificar_acta(st, controller):
    ids = []
    criterios = controller.criterios
    st.title("CALIFICACIÓN DE ACTAS ")
    st.subheader("Selecciona el ID del estudiante a calificar")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
    if (seleccion != None):
        d_calificaciones = controller.calificaciones
        d_calificaciones = d_calificaciones.get(seleccion)
        st.text("Estás calificando a "+str(controller.nombres.get(seleccion)))
        st.subheader("Seleccione bloque criterios a calificar")
        seleccion_2 = st.selectbox("Selección:", criterios.keys())
        if (seleccion_2 != None):
            crt_actual = criterios.get(seleccion_2)
            st.subheader("Seleccione el criterio a calificar")
            seleccion_3 = st.selectbox("Selección:", crt_actual.keys())
            if (seleccion_3 != None):
                nota_crt = st.number_input(seleccion_3, min_value=0.0, max_value=5.0, step=0.1)
                observacion = st.text_input("Observaciones:")
                guardar = st.button("Guardar")
                if guardar:
                    st.text("Se ha calificado a " + str(controller.nombres.get(seleccion)) + " exitosamente")
                    #controller.calificaciones[seleccion] = d_calificaciones