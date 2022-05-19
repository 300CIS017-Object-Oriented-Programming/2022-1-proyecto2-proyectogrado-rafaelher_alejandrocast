import streamlit as st
def search(index, d):
   i = 0
   for key in d:
      if i == index:
         return key
      i+=1

def calificar(i, crt_actual, controller, seleccion, verificar):


def calificar_acta(st, controller):

    ids = []
    nombres = controller.nombres
    criterios = controller.criterios
    st.title("CALIFICACIÓN DE ACTAS ")
    st.subheader("Selecciona el ID del estudiante a calificar")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
    if (seleccion != None):
        st.text("Estás calificando a "+str(nombres.get(seleccion)))
        st.subheader("Seleccione bloque criterios a calificar")
        seleccion_2 = st.selectbox("Selección:", criterios.keys())
        if (seleccion_2 != None):
            crt_actual = criterios.get(seleccion_2)
            i = 0
            st.subheader("Establezca la nota y deje sus comentarios")
            verificar = 0
            while (i<len(crt_actual)):
                actual = search(i, crt_actual)
                nota_crt = st.number_input(actual, min_value=0.0, max_value=5.0, step=0.1)
                st.text("Observaciones:")
                observacion = st.text_input("Observaciones para " + actual)
                guardar = st.button("Guardar")
                if guardar:
                    notas = []
                    tupla = (nota_crt, observacion)
                    notas.append(tupla)
                    i += 1
                    st.text("Se ha calificado a " + str(controller.nombres.get(seleccion)) + " exitosamente")
                #controller.calificaciones[seleccion] = notas