from random import choice, sample

my_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("El primer premio es para el ", choice(my_list))
print("El segundo premio es para el ", choice(my_list))
print("El tercer premio es para el ", choice(my_list))
ganadores=sample(my_list,3)
for i in range (3):
    print("El ganador del premio Nº",i+1," es el ",ganadores[i])