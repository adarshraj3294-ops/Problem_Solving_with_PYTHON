L = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter number: "))
    L.append(x)
    

search = int(input("Enter element to search: "))
found = False
for i in range(len(L)):
    if L[i] == search:
        print(f"Element found at index {i}")
        found = True
        break

if not found:
    print("Element not found")