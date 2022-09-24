sex = input("Anna biologinen sukupuolesi (nainen/mies): ")
hb = int(input("Anna hemoglobiiniarvosi: "))
if sex == "nainen" and hb > 175 or sex == "mies" and hb > 195:
    print("Hemoglobiiniarvosi on korkea.")
elif sex == "nainen" and hb >= 117 or sex == "mies" and hb >= 134:
    print("Hemoglobiiniarvosi on normaali.")
elif sex == "nainen" and hb < 117 or sex == "mies" and hb < 134:
    print("Hemoglobiiniarvosi on alhainen.")
else:
    print("Virheellinen syöte.")
