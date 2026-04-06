n = int(input("Enter your number: " ))


for i in range (n, n*10+1, n):
    print(i)


#another way to do this is:

n = int(input("Enter your number: "))

for i in range(1,11):
    print(f"{n}X{i} = {n * i}")
