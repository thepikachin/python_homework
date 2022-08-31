int1 = input("Anna ensimmäinen kokonaisluku: ")
int2 = input("Anna toinen kokonaisluku: ")
int3 = input("Anna kolmas kokonaisluku: ")

sum = int(int1) + int(int2) + int(int3)
product = int(int1) * int(int2) * int(int3)
average = sum / 3

print(f"Lukujen summa on {sum}, tulo {product} ja keskiarvo {average:.2f}")
