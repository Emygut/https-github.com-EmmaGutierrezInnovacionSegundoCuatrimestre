numero = int(input("Ingrese un número: "))
if numero == 10:
    print("¡Usted ha ganado el sorteo!")


numero = int(input("Ingrese un número: "))
if numero == 10:
    print("¡Usted ha ganado el sorteo!")
elif numero < 10:
    print("¡Falto un poco, seguí participando!")
else:
    print("¡Te pasaste, a seguir intentando!")


dia = input("Ingrese un día de la semana: ").lower()
if dia == "lunes":
    print("Es el comienzo de la semana.")
elif dia == "viernes":
    print("¡Viernes, finalmente el fin de semana está cerca!")
elif dia == "sábado" or dia == "domingo":
    print("Es fin de semana, ¡disfrútalo!")
else:
    print("Este no es un día válido.")


letra = input("Ingrese una letra: ").lower()
if letra in ('a', 'e', 'i', 'o', 'u'):
    print("Es vocal.")






