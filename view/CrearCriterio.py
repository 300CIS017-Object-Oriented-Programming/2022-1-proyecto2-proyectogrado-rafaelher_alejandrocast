



def Nuevo_Criterio(st,controller):
    con = 0
    st.subheader("Nombre del bloque de criterios")
    n_bloque = st.text_input("Nombre del bloque de criterios")
    st.subheader("Criterio y valor porcentual")
    criterio = st.text_input("Criterio")
    porcentaje = st.number_input("Valor porcentual", min_value=0, max_value=100)
    sig = st.button("Siguiente")
    if sig:
        aux = controller.crt_aux
        for key in aux:
            con += aux.get(key)
        if ((con+porcentaje) > 100):
            st.text("No se puede añadir, ya que supera el 100%")
            con = 0
        else:
            controller.crt_aux[criterio] = porcentaje
            st.text("Criterio añadido a "+n_bloque)
            con = 0
        st.text(controller.crt_aux)
    guardar = st.button("Guardar")
    if guardar:
        controller.criterios[n_bloque] = controller.crt_aux
    vaciar = st.button("Vaciar")
    if vaciar:
        controller.crt_aux.clear()


