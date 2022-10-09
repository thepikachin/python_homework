import random

def dicethrow(sides):
    die = random.randint(1,sides)
    return die

die = 0
sides = int(input("Anna nopan tahkojen lukumäärä: "))
while die != sides:
    die = dicethrow(sides)
    print(die)