

""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""
from fpdf import FPDF

from model.EvalAnteproy import EvaluacionAnteproyecto


def instrucciones():
    return """
           Por favor rellenar todos los espacios en este apartado para poder crear el acta. \n\n\n\n\n
           """

def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    st.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png')
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Autor")
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
        controller.nombres[evaluacion_obj.id_estudiante] = evaluacion_obj.nombre
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
    from datetime import datetime
    numact = 1
    st.title('Generar PDF')
    pdf = FPDF()
    pdf.add_page()
    dia = datetime.today().strftime('%Y-%m-%d')
    año = datetime.today().strftime('%Y')
    pdf.set_font('Arial', "B", size=17)
    pdf.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png',15 , 10, 40)
    pdf.cell(200, 10, txt='Facultad de Ingeniería', ln=1, align='C')
    pdf.cell(200, 10, txt='Maestría en Ingeniería', ln=2, align='C')
    pdf.set_font('Arial', "B", size=13)
    pdf.cell(150, 10, txt='ACTA: '+"11"+'-'+año, ln=0, align='L')
    pdf.cell(16, 10, txt='Fecha: ', ln=0, align='L')
    pdf.set_font('Arial', size=13)
    pdf.cell(0, 10, txt=dia, ln=1, align='L')
    pdf.set_font('Arial', "B", size=13)
    pdf.cell(200, 10, txt='ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', ln=1, align='C')
    pdf.set_font('Arial', size=13)



    for posicion in controller.evaluaciones:
        pdf.cell(63, 10, txt='Trabajo de grado denominado: ', ln=0, align='L')
        pdf.cell(80, 10, txt=str(posicion.tema_proyecto), ln=1, align='L')
        pdf.cell(40, 10, txt='Autor: ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.nombre), ln=0, align='L')
        pdf.cell(50, 10, txt='ID: '+str(posicion.id_estudiante), ln=1, align='L')
        pdf.cell(40, 10, txt='Periodo: ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.periodo), ln=1, align='L')
        pdf.cell(40, 10, txt='Director: ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.director), ln=1, align='L')
        pdf.cell(40, 10, txt='Co-Director: ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.co_director), ln=1, align='L')
        pdf.cell(40, 10, txt='Énfasis en:  ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.enfasis), ln=1, align='L')
        pdf.cell(40, 10, txt='Modalidad:  ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.modalidad), ln=1, align='L')
        pdf.cell(40, 10, txt='Jurado 1:  ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.jurado1), ln=1, align='L')
        pdf.cell(40, 10, txt='Jurado 2:  ', ln=0, align='L')
        pdf.cell(100, 10, txt=str(posicion.jurado2), ln=1, align='L')

    pdf.add_page()
    dia = datetime.today().strftime('%Y-%m-%d')
    año = datetime.today().strftime('%Y')
    pdf.set_font('Arial', size=13)
    pdf.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png',15 , 10, 40)
    pdf.cell(200, 10, txt='Facultad de Ingeniería', ln=1, align='C')
    pdf.cell(200, 10, txt='Maestría en Ingeniería', ln=1, align='C')
    pdf.cell(100, 10, txt='ACTA: '+"11"+'-'+año, ln=0, align='L')
    pdf.cell(100, 10, txt='Fecha: '+dia, ln=1, align='L')
    pdf.cell(200, 10, txt='ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', ln=1, align='C')

    enviar_calificacion = st.button('Generar PDF')
    numacta = st.text_input('Nombre del acta', '')
    if enviar_calificacion:
        pdf.output(numacta+'.pdf')
        st.write('ACTA GENERADA')
        st.write('El nombre del acta es:', numacta + '.pdf')
    while numact < 10000:
        numact += 1

# Main call