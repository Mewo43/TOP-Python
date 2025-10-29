try:
    num=int(input("Ingresa un numero: "))

except ValueError as e:
    print("No es un numero")
    print("Error: ",e)
else:
    print(num)
    print("Proceso terminado correctamente")