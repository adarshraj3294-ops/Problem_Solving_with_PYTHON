#Remove duplicates without using set()
L = []
n = int(input("Enter number of elements: "))
for i in range(n):
    x = int(input("Enter number: "))
    L.append(x)
# Remove duplicates
unique_list = []
for i in L:
    if i not in unique_list:
        unique_list.append(i)
print("List after removing duplicates:", unique_list)   