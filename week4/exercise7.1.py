seasons = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
month = int(input("Anna kuukauden järjestysnumero: "))
season = seasons[month-1]
print(f"{month}. kuukausi on vuodenaikana {season}.")

# print(f"{month}. kuukausi on vuodenaikana {seasons[month-1]}")