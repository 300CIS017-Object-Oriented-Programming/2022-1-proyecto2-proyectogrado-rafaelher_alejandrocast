from fpdf import FPDF

def search(clave, d):
   i = 0
   for key in d:
      if key == clave:
         return i
      i+=1

def convertir(ent):
   nota = str(ent)
   letrasM = ['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco']
   letrasm = ['cero', 'uno', 'dos', 'tres', 'cuatro',
              'cinco', 'seis', 'siete', 'ocho', 'nueve']
   p_caracter = letrasM[int(nota[0])]
   s_caracter = letrasm[int(nota[2])]
   cad = p_caracter+" punto "+s_caracter
   return cad

def calificacion_general(id, st, controller):
    acum = 0
    criterio = controller.criterio_persona[id]
    criterio = controller.criterios[criterio]
    notas = controller.calificaciones[id]
    for key_c in criterio:
        for key_n in notas:
            if(key_c == key_n):
                tupla = notas.get(key_n)
                nota_t = ((tupla[0] + tupla[1])/2)
                porcentaje = (criterio.get(key_c)/100)
                acum += nota_t*porcentaje
    acum = float(acum.__round__(1))
    return acum

def imp_lineas(pdf):
    pdf.set_font('Arial', size=11)
    pdf.cell(200, 10, txt="_____________________________________________________________________________________", ln=1,align='L')
    pdf.cell(200, 10, txt="_____________________________________________________________________________________", ln=1,align='L')

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
    class PDF(FPDF):
        def header(self):
            from datetime import datetime
            año = datetime.today().strftime('%Y')
            dia = datetime.today().strftime('%Y-%m-%d')
            pdf.set_font('Arial', "B", size=17)
            pdf.image('https://www2.javerianacali.edu.co/sites/ujc/files/field/image/puj_logo_azul_copia1_0.png', 15,
                      10, 40)
            pdf.cell(200, 10, txt='Facultad de Ingeniería', ln=1, align='C')
            pdf.cell(200, 10, txt='Maestría en Ingeniería', ln=2, align='C')
            pdf.set_font('Arial', "B", size=13)
            pdf.cell(150, 10, txt='ACTA: ' + str(numact) + '-' + año, ln=0, align='L')
            pdf.cell(16, 10, txt='Fecha: ', ln=0, align='L')
            pdf.cell(0, 10, txt=dia, ln=1, align='L')
    pdf = PDF()
    pdf.add_page()
    pdf.auto_page_break
    pdf.set_right_margin(10)
    pdf.alias_nb_pages()
    pdf.set_font('Arial', size=13)
    pdf.set_font('Arial', "B", size=13)
    pdf.cell(200, 10, txt='ACTA DE EVALUACIÓN DE TRABAJO DE GRADO', ln=1, align='C')
    pdf.set_font('Arial', size=13)
    index = search(seleccion, nombres)
    contador = 0
    for posicion in controller.evaluaciones:
        if(contador == index):
            obs_ad = st.text_input("Observaciones adicionales para "+str(nombres[posicion.id_estudiante])+":")
            pdf.multi_cell(0, 7, txt='Trabajo de grado denominado: "'+posicion.tema_proyecto+'"', align='L', border=1)
            pdf.cell(40, 10, txt='Autor: ', ln=0, align='L', border=1)
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
            pdf.cell(40, 10, txt='los Jurados damos las siguientes calificaciones parciales y observaciones (los criterios a evaluar y sus', ln=1, align='L')
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
                        nota_t = ((tupla[0] + tupla[1]) / 2)
                        nota_t = nota_t.__round__(1)
                        obser = tupla[2]
                        veri = True
                        pdf.set_font('Arial', size=11)
                        pdf.cell(150, 10, txt=str('Calificación parcial: '+ str(nota_t)), ln=0, align='L')
                        pdf.cell(100, 10, txt=str('Ponderacion: ' + str(pond)+'%'), ln=1, align='L')
                        pdf.cell(100, 10, txt=str('Observaciones: ' + obser), ln=1, align='L')
                        imp_lineas(pdf)

                        pdf.set_font('Arial', size=11)
                if (veri == False):
                    pdf.set_font('Arial', size=11)
                    pdf.cell(150, 10, txt=str('Calificación parcial: Pendiente' ), ln=0, align='L')
                    pdf.cell(100, 10, txt=str('Ponderacion: ' + str(pond)+'%'), ln=1, align='L')
                    pdf.cell(100, 10, txt=str('Observaciones: Pendiente' ), ln=1, align='L')
                    imp_lineas(pdf)
            nota_final = calificacion_general(posicion.id_estudiante, st, controller)
            pdf.set_font('Arial', "B", size=11)
            pdf.cell(40, 7, txt="Como resultado de estas calificaciones parciales y sus ponderaciones, la calificación del Trabajo de", ln=1, align='L')
            pdf.cell(40, 3, txt="Grado es: "+str(nota_final), ln=1, align='L')
            nota_letras = convertir(str(nota_final))
            pdf.cell(100, 7, txt='', ln=1, align='L')
            pdf.cell(150, 3, txt=str(nota_final), ln=0, align='L')
            pdf.cell(100, 3, txt=nota_letras, ln=1, align='L')
            pdf.cell(150, 5, txt="Números", ln=0, align='L')
            pdf.cell(100, 5, txt="Letras", ln=1, align='L')
            pdf.set_font('Arial', size=12)
            pdf.cell(100, 10, txt=str('Observaciones adicionales: '+obs_ad), ln=1, align='L')
            imp_lineas(pdf)
            pdf.cell(100, 10, txt=str('La calificación final queda sujeta a que se implementen las siguientes correciones: '), ln=1, align='L')
            imp_lineas(pdf)
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
