from random import randrange, randint

print(randrange(10), end="\t")
print(randrange(0, 10), end="\t")
print(randrange(0, 10, 2), end="\t")
print(randint(1, 20))
for i in range(10):
    print(randint(1,10), end=",")