L = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    L.append(x)
G = 0
S = 0
for i in range(len(L)):
    if L[i] > G:
        S = G
        G = L[i]
    elif L[i] > S and L[i] != G:
        S = L[i]
print(f"Second largest element is: {S}")
