import random

randnumber = random.randint(1,10)
givennumber = 0
print(randnumber)
givennumber = int(input("Arvaa numero yhden (1) ja kymmenen (10) väliltä.\n"))
while givennumber != randnumber:
    if givennumber < randnumber:
        givennumber = int(input("Liian pieni arvaus. Arvaa uudestaan.\n"))
    elif givennumber > randnumber:
        givennumber = int(input("Liian suuri arvaus. Arvaa uudestaan.\n"))
print("Oikein.")