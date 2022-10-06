number = 0
allnumbers = []
while number != "":
    number = input("Anna luku: ")
    if number != "":
        number = int(number)
        allnumbers.append(number)
allnumbers.sort(reverse=True)
print("Annetuista luvuista viisi suurinta ovat: ")
for n in allnumbers:
    if allnumbers.index(n) < 5:
        print(n)

#print(allnumbers)