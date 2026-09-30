n = int(input("Enter a number: "))

largest = 0

for i in range(n):
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print(largest)