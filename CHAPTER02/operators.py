# arthematic operators
a = 10
b = 5
print("Addition:", a + b) # 15
print("Subtraction:", a - b) # 5                    
print("Multiplication:", a * b) # 50
print("Division:", a / b) # 2.0
print("Floor Division:", a // b)  # 2 (it gives the quotient without the decimal part)
print("Modulus:", a % b) # 0 (remainder of the division)
print("Exponentiation:", a ** b) # 10000 (10 raised to the power of 5)

# assignment operators
x = 10      
x += 5  # equivalent to x = x + 5
print("After += operator:", x)  # 15
x -= 3  # equivalent to x = x - 3
print("After -= operator:", x)  # 12
x *= 2  # equivalent to x = x * 2                       
print("After *= operator:", x)  # 24
x /= 4  # equivalent to x = x / 4
print("After /= operator:", x)  # 6.0
x //= 2  # equivalent to x = x // 2
print("After //= operator:", x)  # 3.0  
x %= 2  # equivalent to x = x % 2
print("After %= operator:", x)  # 1.0
x **= 3  # equivalent to x = x ** 3
print("After **= operator:", x)  # 1.0 (1 raised to the power of 3 is still 1)  

# comparison operators
a = 10      
b = 5
print("Equal to:", a == b)  # False
print("Not equal to:", a != b)  # True
print("Greater than:", a > b)  # True
print("Less than:", a < b)  # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)  # False

# logical operators
x = True
y = False   
print("Logical AND:", x and y)  # False (both conditions must be true)
print("Logical OR:", x or y)  # True (at least one condition must be true)
print("Logical NOT:", not x)  # False (negates the value of x)

# truth table for 'or' operator
a = True or False
print("True or False:", a)  # True 
print("False or False:", a)  # False
print("True or True:", a)  # True
print("False or True:", a)  # True
# understand it is take true like = i am a human and take false 
# like = i am an animal
# now if we say i am a human or i am an animal then it is true because one of the condition is true 
# also i am a human or i am a human is True because both conditions are true
# but if we say i am a human and i am an animal then it is false because both conditions cannot be true at the same time


# like a statement can't be true and false at the same time but it can be true or false at the same time
