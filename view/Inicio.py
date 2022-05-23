import streamlit as st

def consultar_instrucciones(st, controller):
    st.title("SISTEMA DE GESTIÓN DE NOTAS")
    st.header("-------------------------------------------------------------------------")
    st.header("Bienvenido al software de gestión para calificar los proyectos de grado en la "
                 "Pontificia Universidad Javeriana Cali")
    st.header("-------------------------------------------------------------------------")
    st.subheader("Para empezar:")
    st.subheader('- Debes ingresar los parámetros solicitados en la pestaña "Crear Acta" para '
                 'añadir el proyecto y poder calificarlo')
    st.subheader('- Si deseas ingresar parámetros de calificación nuevos, en la pestaña "Crear Criterios", '
                 'allí deberás darle un nombre a tu sistema de calificación e ingresar los parámetros y '
                 'su valor porcentual')
    st.subheader('- Si deseas calificar un proyecto, en la pestaña "Calificar Actas" seleccionas el ID del autor '
                 'del proyecto a calificar, seleccionas también qué sistema de calificación se usará. '
                 'Solo resta asignar las calificaciones de ambos jurados y una observación general sobre el desempeño '
                 'del proyecto bajo el criterio que está evaluando')
    st.subheader('- Te recomendamos revisar la pestaña "Listar Actas" para que verifiques que todos los parámetros '
                 'están calificados antes de generar el PDF del acta')
    st.subheader('- Finalmente, para generar el PDF del acta, ve a la pestaña "Imprimir Acta" y selecciona el ID '
                 'del autor del proyecto que deseas, ingresas los comentarios generales sobre el proyecto y le das '
                 'un nombre al PDF que se va a generar')