def search(clave, d):
   i = 0
   for key in d:
      if key == clave:
         return i
      i+=1

def Listar_Criterios(st,controller):
    l = []
    st.title("LISTA DE CRITERIOS ")
    st.subheader("Selecciona el nombre del bloque de criterios a listar")
    for key in controller.criterios:
        l.append(key)
    seleccion = st.selectbox("Seleccione:", l)
    index = search(seleccion, l)
    contador = 0
    for key in controller.criterios:
        if (contador == index):
            st.title("Bloque "+key)
            aux = controller.criterios.get(key)
            for key2 in aux:
                st.subheader(key2+ " - "+str(aux.get(key2))+"%")
                st.subheader("--------------------------------------------------------------------------------------------")
        contador += 1