try:
    edad=int(input("Inserta tu edad:"))

    if edad<18:
        print("Eres menor de edad")
    elif edad>=18 and edad<=64:
        print("Eres adulto")
    else:
        print("Eres mayor ")
except ValueError:
    print("Error: Debes introducir un numero ")