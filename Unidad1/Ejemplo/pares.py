for i in range(1,21):
    if(i%2==0):
        print(i, end=", ")
print()
for i in range(2,21,2):
    print(i, end=", ")
pares=[p for p in range(1,21) if p%2==0]
print()
for i in pares:
    print(i, end=", ")