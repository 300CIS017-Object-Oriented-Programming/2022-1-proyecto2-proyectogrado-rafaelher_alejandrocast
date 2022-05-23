# Manual Tecnico

## Desarrollo del sistema para la Gestion de las actas de trabajos de grado.

<br/><br/><br/>
<br/><br/><br/>


## Presentado por:

* Rafael Hermida T.
* Alejandro Castañeda G.





<br/><br/><br/>
<br/><br/><br/>





## Pontificia Universidad Javeriana Cali
## Departamento de Ingerieria
## Ingeniería De Sistemas Y Computación
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

* El siguiente manual técnico guiará a los usuarios que harán soporte a el sistema de gestión de calificación de actas de trabajo de grado, el cual les informará los requerimientos y la estructura que se utilizaron para la contrucción de este sistema, el desarrollo de este entorno web el cual muestra las herramientas necesarias para la contrucción y funcionalidad del sistema.

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

Tu IDE o text editor favorito

PIP

Python 10.0 ó superior

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

| Caso de uso:  | Crear Acta                                                                                                                                                                     |
| ------------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Actores:       | Administrador                                                                                                                                                                  |
| Descripción   | el administrador podra crear las actas con los datos del autor, ID del estudiante, tema del proyecto, periodo, director, co-director, énfasis, modalidad, jurado 1 y jurado 2. |

<br/><br/><br/>

| Caso de uso:  | Crear Criterio                                                                                                             |
| ------------- |----------------------------------------------------------------------------------------------------------------------------|
| Actores:       | Administrador                                                                                                              |
| Descripción   | El administrador registra y almacena la información de cada nuevo bloque de criterios con su valor porcentual y su nombre. |
  
<br/><br/><br/>


 | Caso de uso:  | Calificar Actas                                                                      |
| ------------- |--------------------------------------------------------------------------------------|
| Actores:       | Administrador                                                                        |
| Descripción   | El administrador puede calificar las actas registradas los con bloques de criterios. | 

<br/><br/><br/>


 | Caso de uso:  | Listar actas                                                                                                                                    |
| ------------- |-------------------------------------------------------------------------------------------------------------------------------------------------|
| Actores:       | Administrador                                                                                                                                   |
| Descripción   | El administrador puede listar las actas para verificar si los datos registrados están completos y correctos para realizar la generacón del PDF. | 

<br/><br/><br/>


 | Caso de uso:  | Imprimir actas                                                                                 |
| ------------- |------------------------------------------------------------------------------------------------|
| Actores:       | Administrador                                                                                  |
| Descripción   | El administrador puede imprimir las actas de trabajos de grado indicando el ID del estudiante. |


<br/><br/><br/>


 | Caso de uso:  | Listar Criterios                                                                                                                        |
| ------------- |-----------------------------------------------------------------------------------------------------------------------------------------|
| Actores:       | Administrador                                                                                                                           |
| Descripción   | El administrador puede listar la informacion de cada bloque de criterios para poder verificar si la información de estos está correcta. |


<br/><br/><br/>


 | Caso de uso:  | Eliminar bloque de criterios                                                                                        |
| ------------- |---------------------------------------------------------------------------------------------------------------------|
| Actores:       | Administrador                                                                                                       |
| Descripción   | el administrador podra eliminar los bloque de criterios que ya no necesita y dejar el bloque de criterios principal | 
 
 
<br/><br/><br/>
<br/><br/><br/>
<br/><br/><br/>
 
## Principales funcionalidades
<br/><br/><br/>  

* Registrar actas.

El sistema podrá registar las actas a la base de datos del programa donde se almacenarán los datos del mismo, tales como: nombre del autor, ID del autor, tema del proyecto, periodo, director, co-director énfasis, modalidad, jurado 1 y jurado 2. 

* Crear bloque de criterios

El sistema podrá registrar nuevos bloques de criterios con su respectivo valor porcentual.

* Calificar actas

El sistema podrá calificar las actas creadas con sus respectivos bloques de criterios.

* Listar actas

El sistema podrá listar las actas existentes en el sistema para poder verificar si los datos creados están correctos.

* Imprimir actas

El sistema podrá imprimir las actas listándolas con el ID del autor.

* Listar criterios

El sistema podrá listar los bloques de criterios existentes para saber con cuál de ellos se evaluará cada proyecto de grado.

<br/><br/><br/>
<br/><br/><br/>
<br/><br/><br/>
## Métodos, Entradas y Salidas
<br/><br/><br/>

* Crear acta

Entradas:
* Autor
* ID del autor
* Tema del proyecto
* Periodo
* Director
* Cp-director
* Énfasis
* Modalidad
* Jurado 1
* Jurado 2


Salidas:
* Autor
* ID del autor
* Tema del proyecto
* Periodo
* Director
* Cp-director
* Énfasis
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
