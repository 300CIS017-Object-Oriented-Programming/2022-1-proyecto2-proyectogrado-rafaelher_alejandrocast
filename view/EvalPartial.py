from fpdf import FPDF

from model.EvalAnteproy import EvaluacionAnteproyecto

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""


def instrucciones():
    return """
           Por favor rellenar todos los espacios en este apartado para poder crear el acta. \n\n\n\n\n

           """


def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    st.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png')
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Autor del trabajo de grado")
    evaluacion_obj.id_estudiante = st.text_input("ID Estudiante")
    evaluacion_obj.tema_proyecto = st.text_input("Tema del proyecto")
    evaluacion_obj.periodo = st.text_input("Periodo")
    evaluacion_obj.director = st.text_input("Director")
    evaluacion_obj.co_director = st.text_input("Co-Director")
    evaluacion_obj.enfasis = st.text_input("Énfasis")
    evaluacion_obj.modalidad = st.text_input("Modalidad")
    evaluacion_obj.jurado1 = st.text_input("Jurado 1")
    evaluacion_obj.jurado2 = st.text_input("Jurado 2")


    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Guardar")

    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        controller.agregar_evaluacion(evaluacion_obj)
        st.write("Evaluacion agregada exitosamente")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller


def listar_evaluacion(st, controller):
    """Itera los elementos de evaluacion agregados y los muestra"""
    i = 1
    for evaluacion in controller.evaluaciones:
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


def exp_acta(st, controller):

    st.title('Generar PDF')
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', size=13)
    #pdf.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png')
    #pdf.image('https://www2.javerianacali.edu.co/sites/ujc/files/node/announcement/field_image_box/logo_javeriana_cali_0.jpg')

    pdf.cell(200, 10, txt='Facultad de Ingeniería', ln=1, align='C')
    pdf.cell(200, 10, txt='Maestría en Ingeniería', ln=2, align='C')
    pdf.cell(200, 10, txt='ACTA: ', ln=3, align='L')
    pdf.cell(200, 10, txt='Fecha: ', ln=2, align='R')
    pdf.cell(200, 10, txt=evaluacion_obj[0], ln=2, align='R')



    enviar_calificacion = st.button('Generar PDF')
    numacta = st.text_input('Nombre del acta', '')
    if enviar_calificacion:
        pdf.output(numacta+'.pdf')
        st.write('ACTA GENERADA')
        st.write('El nombre del acta es:', numacta + '.pdf')


# Main call