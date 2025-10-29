try:
    numero = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))
    if (numero > numero2):
        print(numero,"es mayor a ",numero2)
    elif (numero < numero2):
        print(numero,"es menor a ",numero2)
    else:
        print(numero,"es igual a ",numero)
except ValueError:
    print("Error: No has introducido un valor de tipo numérico")