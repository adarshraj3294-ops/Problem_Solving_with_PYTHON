#Find frequency of every element
L = []
n = int(input("Enter number of elements: "))
for i in range(n):
    x = int(input("Enter number: "))
    L.append(x)

frequency = [0]
for i in L:
    frequency[i] = L.count(i)
    

print("Frequency of each element:")
