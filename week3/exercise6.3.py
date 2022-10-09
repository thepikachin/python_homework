def gallontoliter(gallons):
    liters = gallons * 3.785
    return liters

gallons = 0
while gallons >= 0:
    gallons = float(input("Anna bensiinin määrä Yhdysvaltain nestegallonina: "))
    if gallons >= 0:
        liters = gallontoliter(gallons)
        print(f"Bensiinin määrä litroissa on {liters:.3f} litraa.")