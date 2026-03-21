a = input("Enter number 1: ")
b = input("Enter number 2: ")
print("Number a is:", a)
print("Number b is:", b)
# the input() function is used to take input from the user in python. It prompts the user to enter a value and returns it as a string. In this example, we are asking the user to enter two values and then printing them out. The values entered by the user will be stored in the variables a and b, and we can use them later in our program if needed.

# to copy the same line down do shift+alt+down arrow key

print("Sum is", a + b)
# now if we do sum of a and b, it will concatenate the two strings instead of adding them as numbers. To fix this, we need to convert the input values to integers before performing the addition.  
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))      
print("Sum is", a + b)
# now the input values are converted to integers using the int() function, and the addition will