# tuple is like a list but is immutable like a string.

a = (34, 78, 98, 900)
print(type(a))  # this will print the type of the variable a which is tuple.

a =()
# this is an empty tuple and we can also create a tuple with one element but we have to add a comma after the element to indicate that it is a tuple and not just a variable.
print(type(a))  # this will print the type of the variable a which is tuple.

a =(34)
# here the type will be classified as class int and not as a tuple
# cause this is literally just a number in a bracket

print(type(a))  # this will print the type of the variable a which is int because it is not a tuple but just a variable.


# now if we want python to understand it as tuple we will write like this
a =(34,)
print(type(a))  # this will print the type of the variable a which is tuple because



#  we can use same variable to allocate different strings to them cause we will do print function after every variable anyways and python runs code line by line so no problem,
#  but yeah in list there is no issue as such


# a = ( 76, 84555, 984665, False, "nisha", " rohan")
# a[0] = 45  # this will give an error because tuples are immutable which means we cannot change the values of the elements in a tuple but we can change the values of the elements in a list because lists are mutable.
print(a)