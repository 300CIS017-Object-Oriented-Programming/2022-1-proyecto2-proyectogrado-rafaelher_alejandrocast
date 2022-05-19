
def search(clave, d):
   i = 0
   for key in d:
      if key == clave:
         return i
      i+=1


def Listar_Criterios(st,controller):
    ids = []
    nombres = controller.nombres
    st.title("LISTA DE CRITERIOS ")
    st.subheader("Selecciona el ID del estudiante a listar")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)

    """Itera los elementos de evaluacion agregados y los muestra"""
    i = 1
    index = search(seleccion, nombres)
    contador = 0
    for evaluacion in controller.evaluaciones:
        if (contador == index):
            st.title("ACTA NÚMERO "+str(i))

            st.subheader("Nombre")
            st.write(evaluacion.nombre)
       # with col1:
            st.subheader("ID Estudiante")
            st.write(evaluacion.id_estudiante)
        #with col1:
            st.subheader("Tema del proyecto")
            st.write(evaluacion.tema_proyecto)
        #with col1:
            st.subheader("Periodo")
            st.write(evaluacion.periodo)
        #with col1:
            st.subheader("Director")
            st.write(evaluacion.director)
        #with col1:
            st.subheader("Co-Director")
            st.write(evaluacion.co_director)
        #with col1:
            st.subheader("Énfasis")
            st.write(evaluacion.enfasis)
        #with col1:
            st.subheader("Modalidad")
            st.write(evaluacion.modalidad)
        #with col1:
            st.subheader("Jurado 1")
            st.write(evaluacion.jurado1)
        #with col1:
            st.subheader("Jurado 2")
            st.write(evaluacion.jurado2)
        i += 1
        contador += 1