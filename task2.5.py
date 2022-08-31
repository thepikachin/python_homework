import math

leiviska = input("Anna leiviskät: ")
naula = input("Anna naulat: ")
luoti = input("Anna luodit: ")

leiviskatotal = float(leiviska) * 20 * 32 * 13.3
naulatotal = float(naula) * 32 * 13.3
luotitotal = float(luoti) * 13.3
total = leiviskatotal + naulatotal + luotitotal
kilogramstotal = math.floor(total / 1000)
gramstotal = total - (kilogramstotal * 1000)

print(f"Massa nykymittojen mukaan:\n{kilogramstotal} kilogrammaa ja {gramstotal:.2f} kilogrammaa")