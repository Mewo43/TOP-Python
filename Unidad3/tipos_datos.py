try:
    numero=float(input("Escribe un numero:"))
    print("Numero como entero:",int(numero))
    print("Numero como cadena:",str(numero))
    print("El valor ingresado no es un numero")
    cadena=(input("Escribe una cadena que contenga un numero:"))
    suma=int(cadena) + 2
    print("Suma de una cadena combertida a numero:",suma)
except ValueError:
    print("El valor ingresado no es un numero")
except TypeError:
    print("El valor ingresado no es un numero")