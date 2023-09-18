suma = 0
numero = int(input("Ingrese un número (o -1 para salir): "))
while numero != -1:
    suma += numero
    numero = int(input("Ingrese otro número (o -1 para salir): "))
print("La sumatoria de los números ingresados es:", suma) 

2.Contar números mayores, menores e iguales a 0 con estructura FOR:

cantidad = int(input("Ingrese la cantidad de números a introducir: "))
numeros_mayores = 0
numeros_menores = 0
numeros_iguales = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero > 0:
        numeros_mayores += 1
    elif numero < 0:
        numeros_menores += 1
    else:
        numeros_iguales += 1

print("Números mayores que 0:", numeros_mayores)
print("Números menores que 0:", numeros_menores)
print("Números iguales a 0:", numeros_iguales)

3. Identificar vocales con estructura WHILE:

while True:
    caracter = input("Ingrese un carácter (o 0 para salir): ").lower()
    if caracter == '0':
        break
    if caracter in 'aeiouáéíóú':
        print("VOCAL")
    else:
        print("NO VOCAL")
Suma y media de números con estructura WHILE:

suma = 0
contador = 0

while True:
    numero = float(input ("Ingrese un número (o 0 para salir): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print("La suma de los números ingresados es:", suma)
    print("La media de los números ingresados es:", media)
else:
    print("No se ingresaron números.")


