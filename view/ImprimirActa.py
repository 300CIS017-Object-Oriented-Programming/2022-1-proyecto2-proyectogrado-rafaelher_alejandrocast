from fpdf import FPDF

def search(clave, d):
   i = 0
   for key in d:
      if key == clave:
         return i
      i+=1

def imp_acta(st, controller):
    from datetime import datetime
    numact = 1
    st.title('Generar PDF')
    pdf = FPDF()
    pdf.add_page()
    ids = []
    nombres = controller.nombres
    st.title("CALIFICACIÓN DE ACTAS ")
    st.subheader("Selecciona el ID del estudiante a Imprimir")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
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
    index = search(seleccion, nombres)
    contador = 0
    for posicion in controller.evaluaciones:
        if(contador == index):
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
    """
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
    """
    enviar_calificacion = st.button('Generar PDF')
    numacta = st.text_input('Nombre del acta', '')
    if enviar_calificacion:
        pdf.output(numacta+'.pdf')
        st.write('ACTA GENERADA')
        st.write('El nombre del acta es:', numacta + '.pdf')
    while numact < 10000:
        numact += 1
