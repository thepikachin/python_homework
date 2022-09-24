cabinclass = input("Anna laivan hyttiluokka: ")
if cabinclass == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif cabinclass == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif cabinclass == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cabinclass == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
