n = int(input("Enter your number: "))

i = 1
while i< (n+1):
    print(f" sum till {n} is : {(n*(n+1))/2}")
    i += 1
    break



## SECOND WAY
n = int(input("Enter your number: "))

i = 1
sum = 0
while (i<=n):
    sum += i
    
    print (sum)
    i += 1



