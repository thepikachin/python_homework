number = 0
small = large = ""
while number != "":
    number = input("Anna luku: ")
    if number == "":
        break
    if small == "" or float(number) < float(small):
        small = number
    if large == "" or float(number) > float(large):
        large = number
print(f"Antamistasi numeroista suurin on {large} ja pienin {small}")