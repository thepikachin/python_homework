def nonodd(integerlist):
    nonoddlist = []
    for i in integerlist:
        if i % 2 == 0:
            nonoddlist.append(i)
    return nonoddlist

integerlist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
nonoddlist = nonodd(integerlist)
print(f"Muokkaamaton lista kokonaislukuja näyttää tältä:\n{integerlist}")
print(f"Parittomat luvut karsittuna lista näyttää tältä:\n{nonoddlist}")