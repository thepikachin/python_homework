def nonodd(integerlist):
    for i in integerlist:
        if i % 2 == 0:
            integernonodd.append(i)
    return integernonodd

integerlist = [1, 1, 2, 3, 5, 8, 13]