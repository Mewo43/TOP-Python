import sys
lista=[1,2,3,4]
try:
    for n in lista:
        print(n)
except IndexError as e:
    print("Error: ",e)
else:
    print("Finalizado sin errores")
finally:
    sys.exit()
