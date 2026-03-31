list = ["nisha", 987, 76.983, True, "harsh"]
print(list[0])

list[0] = "apples"
print(list)   #this will print the entire list with the updated value of the first element which is "apples" instead of "nisha"
# lists are mutable which means we can change the values of the elements in the list but we cannot change the values of the elements in a string because strings are immutable.
# so the original list is chnaged




# name = "nisha"
# print(name[0])   #this will print the first letter of the string which is "n"
# but if we try to change the value of the first letter of the string it will give
# an error because strings are immutable which means we cannot change the values of the elements in a string but we can change the values of the elements in a list because lists are mutable.
# name[0] = "h" 
# print(name[0])   #this will give an error because we cannot change the value of the first letter of the string which is "n" to "h" because strings are immutable.   



print(list[1:3])