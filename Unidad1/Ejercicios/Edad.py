

while(True):
    edad = int(input("Ingresa un numero: "))
    if(edad < 120 and edad > 0):
        break
    print("Edad invalidad, por favor intentelo de nuevo")

if(edad <= 15 and edad >= 1):
    print("Eres un ninio/a")
if(edad <= 21 and edad >= 16):
    print("Eres un adolescente")
if(edad <= 22 and edad >= 35):
    print("Eres un joven")
if(edad <= 50 and edad >= 36):
    print("Eres un maduro/a ")
if(edad <=60  and edad >= 51):
    print("Eres de mediana edad")
if(edad <= 80 and edad >= 61):
    print("Eres mayor")
if(edad <= 100 and edad >= 81):
    print("Eres viejo")
if(edad > 100):
    print("Eres centenario/a")