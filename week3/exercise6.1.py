import random

def dicethrow():
    die = random.randint(1,6)
    return die

die = 0
while die != 6:
    die = dicethrow()
    print(die)