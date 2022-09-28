import random

givenpoints = int(input("Kuinka paljon pisteitä arvotaan (Suurempi pistemäärä antaa tarkemman likiarvon piille)? "))
totalpoints = withincircle = 0
while totalpoints < givenpoints:
    xcoord = random.uniform(-1,1)
    ycoord = random.uniform(-1,1)
    if xcoord * xcoord + ycoord * ycoord < 1:
        withincircle = withincircle + 1
    totalpoints = totalpoints + 1
piestimate = 4 * withincircle / givenpoints
print(f"Piin likiarvo on {piestimate}")