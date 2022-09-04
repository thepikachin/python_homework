sander = int(input("Anna kuhan pituus senttimetreinä: "))
if sander < 37:
    under = 37 - sander
    print("Kuhasi on alamittainen. Laske kuha takaisin järveen.")
    print(f"Alimmasta pyyntimitasta puuttuu {under} senttimetriä.")