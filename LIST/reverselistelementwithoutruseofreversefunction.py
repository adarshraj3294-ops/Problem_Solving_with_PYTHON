L = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    L.append(x)



for i in range(len(L) - 1, -1, -1):
    print(L[i])