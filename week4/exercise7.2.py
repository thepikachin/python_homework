names = set()
name = "null"
while name != "":
    name = input("Anna nimi: ")
    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    if name != "":
        names.add(name)
print(f"Tässä antamasi nimet:")
for name in names:
    print(name)