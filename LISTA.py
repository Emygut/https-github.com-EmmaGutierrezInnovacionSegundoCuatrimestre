# 1)Crear una lista de nombres de familia ficticios y 6. Mostrar todas las listas. 
nombres_familia = ["García", "López", "Rodríguez", "Pérez", "Martínez", "González", "Hernández", "Flores", "Ramírez", "Díaz"]#En este ejemplo, he creado una lista llamada nombres familia que contiene nombres ficticios de familias.
print (nombres_familia)
# 2) crear una lista en Python con los valores de temperatura para un mes completo. En este caso, usaré valores ficticios para representar las temperaturas diarias de un mes de enero:
temperaturas_enero = [15.2, 16.5, 14.8, 13.7, 11.9, 10.3, 12.6, 14.2, 15.7, 17.3, 18.9, 20.1, 21.5, 22.8, 23.4, 24.6, 25.2, 23.9, 21.7, 18.5, 16.4, 14.2, 13.1, 12.7, 14.3, 16.8, 17.9, 19.2, 20.6, 22.1, 23.5]
print (temperaturas_enero)
# 3) Con los nombres de ciudades que hayan visitado ejemplo de cómo crear una lista en Python con nombres de ciudades que hayas visitado:
Ciudades_visitadas = ["Nueva York", "París", "Tokio", "Londres", "Roma", "Sídney", "San Francisco", "Berlín", "Barcelona", "Río de Janeiro"]
print (Ciudades_visitadas)
#4)Con las fechas y nombres de eventos importantes de su vida
#una lista en Python que contendría fechas y nombres de eventos importantes. Aquí tienes un ejemplo genérico:
eventos_importantes = ["fecha", '26 /09/1960', "nombre", "Mi nacimiento",
    "fecha", '15/06/ 1983', "nombre","Graduación universitaria",
    "fecha", '26/08/1982', "nombre", "Primer trabajo"
]
print (eventos_importantes)
# LUEGO
#1)Ordenar alfabéticamente la lista de los nombres de familia con codificación Python
#nombres_familia = ["García", "López", "Rodríguez", "Pérez", "Martínez", "González", "Hernández", "Flores", "Ramírez", "Díaz"]
nombres_familia_ordenados = sorted(nombres_familia)
print (nombres_familia_ordenados)
#2)Ordenar ascendentemente la lista de temperaturas. 
#ordenar la lista de temperaturas en orden ascendente utilizando el método sort () de Python
temperaturas_enero = [15.2, 16.5, 14.8, 13.7, 11.9, 10.3, 12.6, 14.2, 15.7, 17.3, 18.9, 20.1, 21.5, 22.8, 23.4, 24.6, 25.2, 23.9, 21.7, 18.5, 16.4, 14.2, 13.1, 12.7, 14.3, 16.8, 17.9, 19.2, 20.6, 22.1, 23.5]
temperaturas_enero_ordenados = sorted(temperaturas_enero)
print (temperaturas_enero_ordenados)
#3)  De la lista temperaturas_enero = [15.2, 16.5, 14.8, 13.7, 11.9, 10.3, 12.6, 14.2, 15.7, 17.3, 18.9, 20.1, 21.5, 22.8, 23.4, 24.6, 25.2, 23.9, 21.7, 18.5, 16.4, 14.2, 13.1, 12.7, 14.3, 16.8, 17.9, 19.2, 20.6, 22.1, 23.5]
#Agregar en la lista de temperaturas orginal, las temperaturas de los 15 días del mes siguiente Febrero 
#con a la lista original utilizando el método extend() de Python
temperaturas_enero = [15.2, 16.5, 14.8, 13.7, 11.9, 10.3, 12.6, 14.2, 15.7, 17.3, 18.9, 20.1, 21.5, 22.8, 23.4, 24.6, 25.2, 23.9, 21.7, 18.5, 16.4, 14.2, 13.1, 12.7, 14.3, 16.8, 17.9, 19.2, 20.6, 22.1, 23.5]
# Suponiendo que tienes una lista de temperaturas del mes siguiente
temperaturas_febrero = [20.3, 21.1, 19.8, 18.5, 17.2, 16.4, 15.6, 16.8, 18.2, 19.7, 21.5, 23.0, 24.5, 25.2, 24.0]
# Agregar las temperaturas de febrero a la lista de enero
temperaturas_enero.extend(temperaturas_febrero)
temperatura_enero_parte_febrero = temperaturas_enero.extend(temperaturas_febrero)
print(temperatura_enero_parte_febrero)
#4) Para eliminar elementos específicos de una lista en Python, puedes utilizar el método. remove () en un bucle for. Aquí tienes un ejemplo de cómo podrías hacerlo para quitar los nombres de tus abuelos de la lista nombres_familia:
nombres_familia = ["Gutierrez", "Fedrizzi", "Rodríguez", "Pérez", "Martínez", "González", "Hernández", "Flores", "Ramírez", "Díaz"]
nombres_abuelos = ["Gutierrez", "Fedrizzi"]  
#Nombres de los abuelos que deseas quitar
for nombre in nombres_abuelos:
 if nombre in nombres_familia:
    nombres_familia. remove(nombre)
print (nombres_familia)
#5)   Quitar con codificación Python  de la lista de ciudades la ciudad menos linda que hayas visitado. De la listia ciudades_visitadas = ["Nueva York", "París", "Tokio", "Londres", "Roma", "Sídney", "San Francisco", "Berlín", "Barcelona", "Río de Janeiro"]
ciudades_visitadas = ["Nueva York", "París", "Tokio", "Londres", "Roma", "Sídney", "San Francisco", "Berlín", "Barcelona", "Río de Janeiro"]
print (ciudades_visitadas)
# Supongamos que la ciudad menos linda es la última de la lista
ciudad_menos_linda = ciudades_visitadas [-1]
# Eliminar la ciudad menos linda de la lista
ciudades_visitadas.remove(ciudad_menos_linda)
print(ciudades_visitadas)
print(ciudad_menos_linda)