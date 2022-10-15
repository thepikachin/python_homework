airports = {}
option = airport = icao = ""
while option != "lopeta":
    option = str(input("Jos haluat syöttää uuden lentokentän, kirjoita 'syötä' ja paina Enter.\n"
                       "Jos haluat hakea olemassa olevan lentokentän tiedot, kirjoita 'hae' ja paina Enter.\n"
                       "Jos haluat lopettaa, kirjoita 'lopeta' ja paina Enter.\n"))
    if option != "lopeta":
        if option == "syötä":
            icao = str(input("Anna lentoaseman ICAO-koodi: "))
            airport = str(input("Anna lentoaseman nimi: "))
            airports[icao] = airport
        elif option == "hae":
            search = str(input("Anna haluamasi lentoaseman ICAO-koodi: "))
            if search in airports:
                print(f"Lentokenttä {search} on {airports[search]}")
            else:
                print(f"Lentokenttää {search} ei löydy tietokannasta.")
        else:
            print("Virheellinen syöte")