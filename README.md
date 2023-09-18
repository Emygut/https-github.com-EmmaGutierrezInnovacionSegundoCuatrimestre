# https-github.com-EmmaGutierrezInnovacionSegundoCuatrimestre
#                           EVIDENCIA 7
#     Ejercicios Listas:
#  Crear cuatro listas:
1. Con los nombres de su familia.
2. Con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).
3. Con los nombres de ciudades que hayan visitado.
4. Con las fechas y nombres de eventos importantes de su vida.
#  Luego:
1. Ordenar alfabéticamente la lista de los nombres de familia.
2. Ordenar ascendentemente la lista de temperaturas.
3. Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
4. Quitar de la lista de los nombres de familia, a tus abuelos.
5. Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.
6. Mostrar todas las listas.
#  Ejercicios Tuplas:
Crear tres tuplas con datos random. 
Crear una lista que las contenga y mostrarla.
#  Ejercicio Diccionarios:
# Crear el siguiente diccionario:
#  Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.
Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)

#  Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
Ambos deben ser mostrados.

# ACLARACIÓN:
Los datos no deben ser reales

#                           EVIDENCIA 8
# Ejercicios Estructuras Condicionales:
# Resolver cada enunciado utilizando las estructuras IF – ELSE – ELIF, según usted crea correspondiente:
1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha
ganado el sorteo!
2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco, seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!
3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.

#   Ejercicios Estructuras Repetitivas:
#   Resolver cada enunciado utilizando las estructuras FOR – WHILE, según usted crea correspondiente:

1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar hasta que se ingrese -1.
2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un cero.
4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.


#                           EVIDENCIA 9
#    Ejercicios clases:
1. Crear todas las clases que fueran necesarias para iniciar un proceso de desarrollo de software de la siguiente situación:
Una empresa privada que se dedica a la venta de cursos de oficios, desea desarrollar un sistema web para poder publicar su oferta académica. Dicho sistema debe mostrar una serie de cursos disponibles. 
Por cada curso se deberá visualizar la fecha de comienzo, título, descripción, objetivos, programa, costo, duración en meses, foto y estado (disponible o no disponible, en base a su estado deberán verse o no en el sitio). A su vez, cada curso pertenece a alguna de las siguientes categorías (Inicial, Intermedio, Avanzado). Por otro lado, los cursos contienen un conjunto de clases, en donde por cada clase se debe mostrar la fecha, título, contenido, URLDrive. 
Cada clase de un curso la dicta un docente, y este puede participar en el dictado de varias clases y de varios cursos. De cada docente se desea guardar su apellido, nombre, dni, fecha nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email. 
Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email), además de confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo automático al email registrado. 
Los usuarios públicos registrados pueden inscribirse a uno o más cursos. Además, el sitio deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán interacción con el sistema: Administrador, Docente. Los usuarios también deben tener asociado un estado (Activo / Inactivo).
Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras, donde se deberá visualizar: Foto, título del curso, duración, costo. Una vez confirmados los ítems del carrito, deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de crédito/débito y transferencia bancaria; a fin de tener más datos acerca de los medios de pago, deberán registrarse los datos básicos de tarjetas y transferencias). Al confirmar la compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el monto total. Dada la consigna anterior, se pide: identificar, analizar y documentar los requisitos según el formato de historias de usuario. 
Para modelar esta situación en Python, podemos crear las siguientes clases que representan los elementos principales del sistema. También se puede considerar utilizar un enfoque de bases de datos para almacenar estos datos, pero aquí te proporcionaré las clases Python para representar la estructura del sistema:

#                           EVIDENCIA 10
#  Ejercicios de Herencia
1. Crear todas las clases que fueran necesarias para iniciar un proceso de desarrollo de software de la siguiente situación:
Una empresa privada que se dedica a la venta de cursos de oficios, desea desarrollar un sistema web para poder publicar su oferta académica. Dicho sistema debe mostrar una serie 
de cursos disponibles. 
Por cada curso se deberá visualizar la fecha de comienzo, título, descripción, objetivos, programa, costo, duración en meses, foto y estado (disponible o no disponible, en base a su 
estado deberán verse o no en el sitio). A su vez, cada curso pertenece a alguna de las siguientes categorías (Inicial, Intermedio, Avanzado). Por otro lado, los cursos contienen un 
conjunto de clases, en donde por cada clase se debe mostrar la fecha, título, contenido, URLDrive. 
Cada clase de un curso la dicta un docente, y este puede participar en el dictado de varias clases y de varios cursos. De cada docente se desea guardar su apellido, nombre, dni, fecha 
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email. 
Por otra parte, los interesados en inscribirse a un curso deberán crearse una cuenta de usuario final, donde deberán registrar su datos personales (nombre, apellido, dni, dirección, fecha 
nacimiento, dirección, localidad, código postal, provincia, teléfono celular, email), además de confirmar y reconfirmar una clave de acceso. Para la activación de la cuenta de usuario final se 
deberá validar que el email sea verdadero y esté en funcionamiento, enviando un correo automático al email registrado. 
Los usuarios públicos registrados pueden inscribirse a uno o más cursos. Además, el sitio deberá proveer la posibilidad de registrar 2 roles más de usuarios quienes también tendrán 
interacción con el sistema: Administrador, Docente. Los usuarios también deben tener asociado un estado (Activo / Inactivo). 
Por último, los usuarios finales podrán agregar uno o más cursos en un carrito de compras, donde se deberá visualizar: Foto, título del curso, duración, costo. Una vez confirmados los 
ítems del carrito, deberá seleccionar el medio de pago, los cuales pueden ser: Tarjeta de crédito/débito y transferencia bancaria; a fin de tener más datos acerca de los medios de 
pago, deberán registrarse los datos básicos de tarjetas y transferencias). Al confirmar la compra, se deberá registrar además la fecha de compra, el usuario que realiza la compra y el 
monto total. Dada la consigna anterior, se pide: identificar, analizar y documentar los requisitos según el formato de historias de usuario. Para la creación de las historias, hacer uso 
del repositorio Github.
Partiendo de la base del ejercicio de CLASES, se pide: 
 Que la clase Docente, sea herencia de la clase Usuario.
 Generar una clase nueva que sea compra y contenga: 
o Id_Compra
o Id_Carrito_Compra
o Id_Medios_Pago
o Id_Usuario
o Fecha
o Monto_Total
 Generar una clase de Medios de Contacto que contenga:
o Id_MedioContacto
o Fecha
o Email
o Telefono
o Direccion
o Nombre
 Generar una clase que sea: Tipos de Medio de Contacto en formato enum:
o WhatsApp
o Correo electrónico
o Call center
o Referido interno
 La clase Tipos de Medio de Contacto debe heredar de Medios de contacto

