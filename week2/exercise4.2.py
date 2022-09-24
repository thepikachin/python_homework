inches = 0
while inches >= 0:
    inches = float(input("Kuinka monta tuumaa haluat muuttaa senttimetreiksi?\n"))
    if inches >= 0:
        centimeters = inches * 2.54
        print(f"{inches} tuumaa on {centimeters} senttimetriä.")
print("Ohjelma lopetettu")