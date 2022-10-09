def integersum(integers):
    sum = 0
    for i in integers:
        sum = sum + i
    return sum

integers = [1, 1, 2, 3, 5, 8, 13]
sum = integersum(integers)
print(f"Listan kokonaislukujen summa on {sum}.")
