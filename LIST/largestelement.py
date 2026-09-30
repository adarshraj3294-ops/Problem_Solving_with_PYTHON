L=[]
n = int(input("Enter number of element"))
for i in range(n):
    x = int(input("Enter number"))
    L.append(x)
G=L[0]
for i in L:
    if i>G:
        G=i
print("largest element = ",G)        
                