""" Este archivo contine las funcionalidades de la vista relacionado con la evaluacion de los anteproyectos"""
from fpdf import FPDF

from model.EvalAnteproy import EvaluacionAnteproyecto
from view.ImprimirActa import calificacion_general

def verificar_vacio(evaluacion_obj):
    if(evaluacion_obj.nombre == ''):
        return True
    if(evaluacion_obj.id_estudiante == ''):
        return True
    if(evaluacion_obj.tema_proyecto == ''):
        return True
    if (evaluacion_obj.periodo == ''):
        return True
    if (evaluacion_obj.director == ''):
        return True
    if (evaluacion_obj.enfasis == ''):
        return True
    if (evaluacion_obj.co_director == ''):
        return True
    if (evaluacion_obj.modalidad == ''):
        return True
    if (evaluacion_obj.jurado1 == ''):
        return True
    if (evaluacion_obj.jurado2 == ''):
        return True
    return False

def verificar_id(controller, id_):
    dic = controller.nombres
    for key in dic:
        if(key == id_):
            return True
    return False

def instrucciones():
    return """
           Por favor rellenar todos los espacios en este apartado para poder crear el acta. \n\n\n\n\n
           """

def id_sinLetras(id):
    numeros = "1234567890"
    condicion = False
    for caracter in id:
        for numero in numeros:
            if (caracter == numero):
                condicion = True
        if(condicion == False):
            return True
        condicion = False
    return False

def agregar_evaluacion(st, controller):
    # Objecto que modelará el formulario
    evaluacion_obj = EvaluacionAnteproyecto()
    evaluacion_obj.nombre = st.text_input("Autor")
    evaluacion_obj.id_estudiante = st.text_input("ID Estudiante")
    evaluacion_obj.tema_proyecto = st.text_input("Tema del proyecto")
    evaluacion_obj.periodo = st.text_input("Periodo")
    evaluacion_obj.director = st.text_input("Director")
    codirector= st.radio("¿Existe Co-Director para el proyecto?", ('Sí','No'))
    if codirector == 'Sí':
        evaluacion_obj.co_director = st.text_input("Co-Director")
    else:
        evaluacion_obj.co_director = 'NA'
    evaluacion_obj.enfasis = st.text_input("Énfasis")
    evaluacion_obj.modalidad = st.radio("Escoja la modalidad", ('Investigación', 'Aplicado'))
    evaluacion_obj.jurado1 = st.text_input("Jurado 1")
    evaluacion_obj.jurado2 = st.text_input("Jurado 2")
    # TODO
    # Agregar campo para leer el tema y la versión de la evaluación del proyecto
    enviado_btn = st.button("Guardar")
    # Cuando se oprime el boton se agrega a la lista
    if enviado_btn:
        vacio_idt = verificar_vacio(evaluacion_obj)
        if (vacio_idt == False):
            cond_idt = verificar_id(controller, evaluacion_obj.id_estudiante)
            if (cond_idt == False):
                if (id_sinLetras(evaluacion_obj.id_estudiante) == False):
                    controller.agregar_evaluacion(evaluacion_obj)
                    st.write("Acta agregada exitosamente")
                    controller.nombres[evaluacion_obj.id_estudiante] = evaluacion_obj.nombre
                    controller.calificaciones[evaluacion_obj.id_estudiante] = {}
                    controller.criterio_persona[evaluacion_obj.id_estudiante] = 'Actuales'
                else:
                    st.write("No se puede generar el acta porque el id contiene caracteres diferentes a números")
            else:
                st.write("No se puede generar el acta porque el id ya se encuentra registrado en el sistema")
        else:
            st.write("No se puede generar el acta porque hay criterios vacíos")
    # Retorna el controlador pq solo las colecciones se pasan en python por referencia,
    # entonces de esta manera se actualiza el controlador en la vista principal
    return controller

def search(clave, d):
   i = 0
   for key in d:
      if key == clave:
         return i
      i+=1

def listar_evaluacion(st, controller):
    ids = []
    nombres = controller.nombres
    criterios = controller.criterios
    notas = controller.calificaciones
    st.title("LISTA DE ACTAS ")
    st.subheader("Selecciona el ID del estudiante a listar")
    for calificacion in controller.evaluaciones:
        ids.append(calificacion.id_estudiante)
    seleccion = st.selectbox("Seleccione:", ids)
    """Itera los elementos de evaluacion agregados y los muestra"""
    i = 1
    e = 0
    index = search(seleccion, nombres)
    contador = 0
    for evaluacion in controller.evaluaciones:
        if (contador == index):
            st.title("ACTA NÚMERO "+str(i))
            notas = notas[evaluacion.id_estudiante]
            criterios_p = controller.criterio_persona[evaluacion.id_estudiante]
            dat = criterios[criterios_p]
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
            for key in dat:
                st.subheader(key)
                dat2 = notas.get(key)
                if (dat2 == None):
                    dat2 = 'Por favor Ingresar el valor de la calificación.'
                    st.text(dat2)
                else:
                    st.text((dat2[0] + dat2[1])/2)
            st.subheader("Calificación general")
            st.text(calificacion_general(evaluacion.id_estudiante, st, controller))
        i += 1
        e += 1
        contador += 1