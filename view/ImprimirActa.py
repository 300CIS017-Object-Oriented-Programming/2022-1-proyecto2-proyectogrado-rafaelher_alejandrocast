from fpdf import FPDF

def search(clave, d):
   i = 0
   for key in d:
      if key == clave:
         return i
      i+=1

def calificacion_general(id, st, controller):
    acum = 0
    criterio = controller.criterio_persona[id]
    criterio = controller.criterios[criterio]
    notas = controller.calificaciones[id]
    for key_c in criterio:
        for key_n in notas:
            if(key_c == key_n):
                tupla = notas.get(key_n)
                nota_t = ((tupla[0] + tupla[2])/2)
                porcentaje = (criterio.get(key_c)/100)
                acum += nota_t*porcentaje
    return acum


def header(st,controller,pdf):
    from datetime import datetime
    año = datetime.today().strftime('%Y')
    dia = datetime.today().strftime('%Y-%m-%d')
    pdf.set_font('Arial', "B", size=17)
    pdf.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png',15 , 10, 40)
    pdf.cell(200, 10, txt='Facultad de Ingeniería', ln=1, align='C')
    pdf.cell(200, 10, txt='Maestría en Ingeniería', ln=2, align='C')
    pdf.set_font('Arial', "B", size=13)
    pdf.cell(150, 10, txt='ACTA: '+"11"+'-'+año, ln=0, align='L')
    pdf.cell(16, 10, txt='Fecha: ', ln=0, align='L')
    pdf.cell(0, 10, txt=dia, ln=1, align='L')


def imp_acta(st, controller):
    from datetime import datetime
    st.title('Generar PDF')
    acum = 0
    numact = 1
    ids = []
    nombres = controller.nombres
    st.subheader("Selecciona el ID del estudiante a Imprimir")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
    pdf = FPDF()
    pdf.add_page()
    header(st, controller,pdf)
    pdf.set_font('Arial', size=13)
    pdf.set_font('Arial', "B", size=13)
    pdf.cell(200, 10, txt='ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', ln=1, align='C')
    pdf.set_font('Arial', size=13)
    index = search(seleccion, nombres)
    contador = 0
    for posicion in controller.evaluaciones:
        if(contador == index):
            pdf.cell(63, 10, txt='Trabajo de grado denominado: "', ln=0, align='L')
            pdf.cell(80, 10, txt=' "'+str(posicion.tema_proyecto)+'"', ln=1, align='L')
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
            pdf.set_font('Arial', size=11)
            pdf.cell(40, 10, txt='En atención al desarrollo de este Trabajo de Grado y al documento y sustentación que presentó el(la) autor(a),', ln=1, align='L')
            pdf.cell(40, 10, txt='os Jurados damos las siguientes calificaciones parciales y observaciones (los criterios a evaluar y sus', ln=1, align='L')
            pdf.cell(40, 10, txt='ponderaciones se estipulan en el artículo 7.1 de las Directrices para Trabajo de Grado de Maestría):', ln=1, align='L')

            criterio = controller.criterio_persona[posicion.id_estudiante]
            criterio = controller.criterios[criterio]
            notas = controller.calificaciones[posicion.id_estudiante]
            numeral = 1
            for key_c in criterio:
                veri = False
                pdf.set_font('Arial', "B", size=12)
                pdf.cell(100, 10, txt=str(str(numeral)+'. '+key_c), ln=1, align='L')
                numeral += 1
                pond = criterio.get(key_c)
                for key_n in notas:
                    pdf.set_font('Arial', size=13)
                    if (key_c == key_n):
                        tupla = notas.get(key_n)
                        nota_t = ((tupla[0] + tupla[2]) / 2)
                        jur1 = tupla[1]
                        jur2 = tupla[3]
                        obser = tupla[4]
                        veri = True
                        pdf.set_font('Arial', size=11)
                        pdf.cell(150, 10, txt=str('Calificación parcial: '+ str(nota_t)), ln=0, align='L')
                        pdf.cell(100, 10, txt=str('Ponderacion: ' + str(pond)+'%'), ln=1, align='L')
                        pdf.cell(100, 10, txt=str('Observaciones: ' + obser), ln=1, align='L')
                        pdf.cell(200, 10,txt="_________________________________________________________________________________________",ln=1, align='L')
                        pdf.cell(200, 10,txt="_________________________________________________________________________________________",ln=1, align='L')


                        pdf.set_font('Arial', size=11)
                if (veri == False):
                    pdf.set_font('Arial', size=11)
                    pdf.cell(150, 10, txt=str('Calificación parcial: Pendiente' ), ln=0, align='L')
                    pdf.cell(100, 10, txt=str('Ponderacion: ' + str(pond)+'%'), ln=1, align='L')
                    pdf.cell(100, 10, txt=str('Observaciones: Pendiente' ), ln=1, align='L')
                    pdf.cell(200, 10,txt="_________________________________________________________________________________________",ln=1, align='L')
                    pdf.cell(200, 10,txt="_________________________________________________________________________________________",ln=1, align='L')
        contador += 1
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
    numacta = st.text_input('Nombre del acta', '')
    enviar_calificacion = st.button('Generar PDF')
    if enviar_calificacion:
        pdf.output(numacta+'.pdf')
        st.write('ACTA GENERADA')
        st.write('El nombre del acta es:', numacta + '.pdf')
    while numact < 10000:
        numact += 1
