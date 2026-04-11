## FIRST METHOD

import math

n = int(input("Enter your number: "))

for i in range (1, (n+1)):
    print(f"factorial of {n} is: {math.factorial(n)}")
    break
    pass

#so to use the maths factorial thing we have to import math thing and mention it.
#i was trying to figure out how do i do factorial formula.



## SECOND METHOD

n = int(input("Enter your number: "))
product = 1
for i in range (1, (n+1)):
    product = product * i

print(f"The factorial of {n} is {product}")