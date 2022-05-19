



def Nuevo_Criterio(st,controller):
    d1 = {}
    d2 = {}
    con = 0
    st.subheader("Nombre del bloque de criterios")
    n_bloque = st.text_input("Nombre del bloque de criterios")
    st.subheader("Criterio y valor porcentual")
    criterio = st.text_input("Criterio")
    porcentaje = st.number_input("Valor porcentual", min_value=0, max_value=100)
    sig = st.button("Siguiente")
    if sig:
        for key in d2:
            con += d2.get(key)
        if ((con+porcentaje) > 100):
            st.text_input("No se puede añadir, ya que supera el 100%")
            con = 0
        else:
            d2[criterio] = porcentaje
            st.text("Criterio añadido a "+n_bloque)
            con = 0
        st.text(d2)
    st.button("Guardar")
    st.button("Vaciar")


