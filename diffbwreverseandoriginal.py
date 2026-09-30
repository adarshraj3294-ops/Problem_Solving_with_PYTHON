n = int(input("Enter a number: "))
original = n
r = 0

while n > 0:
    digit = n % 10
    r = r * 10 + digit
    n = n // 10

if r > original:
    print(r - original)
else:
    print(original - r)