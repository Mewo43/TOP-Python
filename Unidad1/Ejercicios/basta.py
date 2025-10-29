
cadena=""
contador=0
while(True):
    palabra = str(input("Introduce una palabra: "))
    cadena+=palabra
    print(cadena)

    if(palabra=="Basta" or palabra==""):
        break
    cadena += ", "
    contador+=1
print("“Has soportado estoicamente",contador ,"preguntas")