L=[]
n = int(input("Enter number of element"))
for i in range(n):
    x = int(input("Enter number"))
    L.append(x)
P=0
N=0
Z=0
for i in L:
    if i>0:
        P+=1
    elif i<0:
        N+=1
    else:
        Z+=1
print("Positive numbers = ",P)
print("Negative numbers = ",N)
print("Zeroes = ",Z)