import time as t
try:
    print("Fichero escrito escrito correctamente")
    contador=int(input("Ingrese un numero: "))
    while(contador<5 or contador>50):
        print("El numero  debe ser mayor que 4 y menor que 51")
        contador=int(input("Ingrese un numero: "))
    for i in range(contador,0,-1):
        print(i)

        t.sleep(0.5)
except ValueError:
    print("El valor introducido debe ser un numero")
