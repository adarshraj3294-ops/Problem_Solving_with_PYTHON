n = int(input("Enter a number: "))
d = int(input("Enter a number: "))
c = 0
while n>0:
    digit = n%10
    if digit==d:
        c =c+1
    n=n//10
print(c)        
    