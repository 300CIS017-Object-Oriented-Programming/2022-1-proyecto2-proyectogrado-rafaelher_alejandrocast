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
        n_igual = False
        for key in aux:
            con += aux.get(key)
            if(key == criterio):
                n_igual = True
        if n_igual:
            st.text("No se puede añadir el criterio, ya que existe uno con el mismo nombre")
        elif ((con+porcentaje) > 100):
            st.text("No se puede añadir, ya que supera el 100%")
            con = 0
        else:
            controller.crt_aux[criterio] = porcentaje
            st.text("Criterio añadido a "+n_bloque)
            con = 0

    guardar = st.button("Guardar")

    if guardar:
        aux = controller.crt_aux
        aux2 = controller.criterios
        n_igual = False
        for key in aux:
            con += aux.get(key)
        for key in aux2:
            if (n_bloque == key):
                n_igual = True
        if n_igual:
            st.text("No se puede añadir el bloque, ya que existe uno con el mismo nombre")
        elif ((con) < 100):
            st.text("No se puede añadir, ya que no llega a el 100%")
            con = 0
        else:
            aux3 = controller.crt_aux.copy()
            controller.criterios[n_bloque] = aux3
            st.text("Bloque " + n_bloque+ " ha sido añadido correctamente")
            controller.crt_aux.clear()

    vaciar = st.button("Vaciar")

    if vaciar:
        controller.crt_aux.clear()
        st.text("Bloque " + n_bloque + " sido vaciado correctamente")
    st.subheader("El bloque "+n_bloque+" quedaría de la siguiente manera")
    aux = controller.crt_aux
    for key in aux:
        st.text(key+" - "+str(aux.get(key))+"%")