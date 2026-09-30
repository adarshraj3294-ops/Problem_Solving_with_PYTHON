s=input("Enter string")
L=s.split()
G=0
for i in L:
    if len(i)>G:
        G=len(i)
print("Length of longest word is:", G)
