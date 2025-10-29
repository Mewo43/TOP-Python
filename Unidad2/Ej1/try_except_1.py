texto=""
try:
    f = open("archivo3.txt","r")
    #texto = f.read()
    f.write("Hola, ke hase")

except IOError as e:
    print("Ocurrio un error: ",e)
else:
    print("Fichero escrito escrito correctamente")
finally:
    f.close()