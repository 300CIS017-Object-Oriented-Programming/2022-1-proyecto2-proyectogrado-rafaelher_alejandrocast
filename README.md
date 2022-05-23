# README

## Desarrollo sistema para la gestión de las actas de trabajos de grado.

<br/><br/><br/>
<br/><br/><br/>

## 	Descripción:
* Este sistema web se realiza para darle gestión y solución a la calificación a el sistema de las actas de grado, ya que estas se estaban calificando directamente desde un archivo Excel. Este programa automatiza las funciones que realiza el administrador o la persona que realiza la calificación de estas actas.


## Guia
* En el manual tecnico se guiara a los usuarios que haran soporte a el sistema de gestion del sistema de calificacion de las actas de trabajo de grado, el cual les informara los requerimientos y la estructura que se utilizaron para la contruccion de este sistema, el desarrollo de este entorno web el cual muestra las herramientas necesarios para la contrucción y funcionalidad del sistema.



## Este sistema fue desarrollado por:

* Rafael Hermida T.
* Alejandro Castañeda G.


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

