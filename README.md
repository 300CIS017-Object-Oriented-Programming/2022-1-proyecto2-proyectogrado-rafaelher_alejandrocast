# Manual Tecnico

## Desarrollo del sistema para la Gestion de las actas de trabajos de grado.

<br/><br/><br/>
<br/><br/><br/>


## Presentado por:

* Rafael Hermida T.
* Alejandro Castañeda G.





<br/><br/><br/>
<br/><br/><br/>





## Universidad Pontificia Javeriana Cali
## Departamento de Ingerieria
## Ingeniria De Sistemas Y Computación
## 2022

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>
  
# Contenido

* Presentación
* Objetivo
* Procesos
* Requisitos del sistema
* Herramientas utilizadas para el desarrollo
* diagrama UML
* Casos de uso
* Principales funcionalidades
* Entradas y Salidas
      
  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>       
        
## Presentación

* El siguiente manual tecnico guiara a los usuarios que haran soporte a el sistema de gestion del sistema de calificacion de las actas de trabajo de grado, el cual les informara los requerimientos y la estructura que se utilizaron para la contruccion de este sistema, el desarrollo de este entorno web el cual muestra las herramientas necesarios para la contrucción y funcionalidad del sistema.

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>       

## Objetivo

* Informar al usuario la estructura y formacion del sistema con el fin que sepan el funcionamiento para realizar el soporte y las modificaciones que sean requeridas por el cliente.

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>       

## Procesos

#### Procesos de entrada.

#### Procesos de salida.

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/> 
  
  
## Requisitos del sistema

* Requisitos de hardware

Equipo, teclado, mouse, monitor

Memoria RAM 8 Gb

Peocesador 1.5 GHz en adelante

* Requisitos de software

Sistema operativo (Windows 7 en adelante)
Your favorite IDE or text editor
PIP
Python 10.0
Streamlit 

  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/> 

## Herramientas utilizadas para el desarrollo

### PYTHON
Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código, se utiliza para desarrollar aplicaciones de todo tipo, ejemplos: Instagram, Netflix, Panda 3D, entre otros. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

Administrado por Python Software Foundation, posee una licencia de código abierto, denominada Python Software Foundation License. Python se clasifica constantemente como uno de los lenguajes de programación más populares.

### PyCharm

PyCharm es un entorno de desarrollo integrado (IDE) utilizado en programación informática, concretamente para el lenguaje de programación Python. Está desarrollado por la empresa checa JetBrains (antes conocida como IntelliJ). Proporciona análisis de código, un depurador gráfico, un probador de unidades integrado, integración con sistemas de control de versiones (VCS), y soporta el desarrollo web con Django, así como la ciencia de datos con Anaconda.

PyCharm es multiplataforma, con versiones para Windows, macOS y Linux. La Community Edition (edición comunitaria) se publica bajo la Licencia apache, y también hay una Professional Edition (edición profesional) con características adicionales publicada bajo una licencia propietaria financiada por suscripción y también una versión educativa.

### Streamlit

Streamlit es una biblioteca Python de código abierto que facilita la creación y el intercambio de hermosas aplicaciones web personalizadas para el aprendizaje automático y la ciencia de datos. En solo unos minutos, puede crear e implementar potentes aplicaciones de datos.


  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/> 
  
## Diagrama UML


![](https://github.com/300CIS017-Object-Oriented-Programming/2022-1-proyecto2-proyectogrado-rafaelher_alejandrocast/blob/main/proyecto2POO.png)



  <br/><br/><br/>
  <br/><br/><br/>
  <br/><br/><br/>
  
## Casos de uso
<br/><br/><br/>

| Caso de uso:  | Crear Acta |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   |el administrador podra crear las actas con los datos del autor, id del estudiante, tema del proyecto, periodo, director, co-director, enfasis, Modalidad, jurado 1, jurado 2|

<br/><br/><br/>

| Caso de uso:  | Crear Criterio |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   |el administrador registra y almacena la información de cada nuevo bloque de criterios con su valor porcentual y su nombre. |
  
<br/><br/><br/>


 | Caso de uso:  | Calificar Actas |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador puede calificar las actas registradas los con bloques de criterios  | 

<br/><br/><br/>


 | Caso de uso:  | Listar actas |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador puede listar las actas para verificar si los datos registrados estan completos y correctos para poder imprimir  | 

<br/><br/><br/>


 | Caso de uso:  | Imprimir actas |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador puede imprimir las actas de trabajos de grado por el numero de id del estudiante |


<br/><br/><br/>


 | Caso de uso:  | listar Criterios |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador puede listar la informacion de cada bloque de criterios para poder verificar si la informacion de estos esta correcta.  |


<br/><br/><br/>


 | Caso de uso:  | eliminar bloque de criterios |
| ------------- |-------------|
| Actores:       | Administrador|
| Descripción   | el administrador podra eliminar los bloque de criterios que ya no necesita y dejar el bloque de criterios principal | 
 
 
<br/><br/><br/>
<br/><br/><br/>
<br/><br/><br/>
 
## Principales funcionalidades
<br/><br/><br/>  

* Registrar actas.

El sistema podra registar las actas a la base de datos de el programa donde se almacenara los datos de este como nombre del autor, id del autor, tema del proyecto, periodo, director, co-director énfasis, modalidad, jurado 1 y jurado 2. 

* Crear bloque de criterios

El sistema podra registrar nuevos bloques de criterios con su respectivo valor porcentual 

* Calificar actas

El sistema podra calificar las actas creadas con sus respectivos bloques de criterios.

* Listar actas

El sistema podra Listar las actas existentes en el sistema para poder verificar si los datos creados estan correctos.

* Imprimir actas

El sistema podra imprimir las actas listandolas con el nombre de el id.

* Listar criterios

El sistema podra listar los bloques de criterios existentes para saber con cual de ellos se evaluara cada proyecto de grado.





<br/><br/><br/>
<br/><br/><br/>
<br/><br/><br/>


## Métodos, Entradas y Salidas
<br/><br/><br/>

* Crear acta

Entradas:
* Autor
* Id del autor
* Tema del proyecto
* Periodo
* Director
* Cp-director
* Enfasis
* Modalidad
* Jurado 1
* Jurado 2


Salidas:
* Autor
* Id del autor
* Tema del proyecto
* Periodo
* Director
* Cp-director
* Enfasis
* Modalidad
* Jurado 1
* Jurado 2


*  Crear Criterio

Entrada:
* Nombre del criterio
* valor porcentual

Salida:
* Nombre del criterio
* valor porcentual

* Imprimir acta

Entrada:
* Observaciones adicionales
* Nombre del acta

Salida:
* Observaciones adicionales
* Nombre del acta
