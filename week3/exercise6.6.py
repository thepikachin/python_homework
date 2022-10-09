import math

# ympyrän pinta-ala on pii * säde ^ 2
def pizzavalue(diameter, price):
    size = math.pi * (diameter / 2) ** 2
    value = price / (size / 10000)
    return value

firstdiameter = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
firstprice = float(input("Anna ensmmäisen pizzan hinta euroina: "))
firstvalue = pizzavalue(firstdiameter, firstprice)
seconddiameter = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
secondprice = float(input("Anna toisen pizzan hinta euroina: "))
secondvalue = pizzavalue(seconddiameter, secondprice)

print(f"Ensimmäinen pizza maksaa {firstvalue:.2f}€ per neliömetri. Toinen pizza maksaa {secondvalue:.2f}€ per neliömetri.")
if firstvalue < secondvalue:
    print("Ensimmäiseksi antamasi pizza on halvempi kokoonsa nähden. Osta se.")
elif firstvalue > secondvalue:
    print("Toiseksi antamasi pizza on halvempi kokoonsa nähden. Osta se.")
else:
    # Tähän tuskin päästään ellei parametrit kummallekin pizzalle ole täsmälleen samat.
    # Mutta onpahan huomioitu.
    print("Pizzat ovat saman arvoisia. Osta kumpi vain.")