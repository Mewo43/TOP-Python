cadena="Hola, aqui programando en Python "
num_vocales=0
vocales=["a","e","i","o","u","A","E","I","O","U"];
for i in cadena:
   if(i in vocales):
       num_vocales+=1

print("Hay ",num_vocales," vocales")
