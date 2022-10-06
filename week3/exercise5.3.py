primenumber = True
yournumber = int(input("Anna luku: "))
for number in range(2,yournumber):
    if yournumber % number == 0:
        primenumber = False
        break
if primenumber == True:
    print(f"Luku {yournumber} on alkuluku.")
else:
    print(f"Luku {yournumber} ei ole alkuluku.")