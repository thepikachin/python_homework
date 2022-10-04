import random

totalrolls = total = 0
dicerolls = int(input("Kuinka monta arpakuutiota heitetään? "))
numbers = []
while totalrolls < dicerolls:
    number = random.randint(1,6)
    totalrolls = totalrolls + 1
    numbers.append(number)
for n in numbers:
    total = total + n
print(f"Arpakuution lukujen summa on {total}")