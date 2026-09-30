L=[]
n = int(input("Enter number of element"))
for i in range(n):
    x = int(input("Enter number"))
    L.append(x)
s=0
for i in range(len(L)):
    s=s+L[i]
print(s)        