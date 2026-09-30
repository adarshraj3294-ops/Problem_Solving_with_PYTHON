L=[]
n = int(input("Enter number of element"))
for i in range(n):
    x = int(input("Enter number"))
    L.append(x)
S=L[0]
for i in L:
    if i<S:
        S=i
print("smallest element = ",S)        
                