
nota1=float(input("Ingrese la primera nota: "))
while(nota1>10 or nota1<0 ):
    print("La nota no es valida")
    nota1 = float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segunda nota: "))
while(nota2>10 or nota2<0):
    print("La nota no es valida")
    nota2 = float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercera nota: "))
while(nota3>10 or nota3<0):
    print("La nota no es valida")
    nota3 = float(input("Ingrese la tercera nota: "))
media=round((nota1+nota2+nota3)/3,2)
print("La media de la nota es: ",media)