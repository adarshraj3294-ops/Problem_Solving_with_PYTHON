n = int(input("Enter a number: "))

snallest = 9
for i in range(n):
    digit = n % 10

    if digit < snallest:
        snallest = digit
        

n = n // 10

print(snallest)