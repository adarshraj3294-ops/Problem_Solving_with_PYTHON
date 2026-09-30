L=[]
n = int(input("Enter number of element"))
for i in range(n):
    x = int(input("Enter number"))
    L.append(x)
E=0
O=0
for i in L:
    if i%2==0:
        E+=1
    else:
        O+=1
print("Even numbers = ",E)
print("Odd numbers = ",O)