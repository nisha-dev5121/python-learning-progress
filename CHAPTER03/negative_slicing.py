name = "Nisha"

print(name[0:3])

print(name[-4:-1])   #this means -1 in  excluded
print(name[1:4])     #this is the same as above but we are counting from the front

# so for negavtive just convert to its positive index and then apply the same logic as above    

print(name[-4:])     #this means start from -4 and go to the end of the string
print(name[:3])      #this means start from the beginning and go to index 3 
print(name[1:])       #this means start from index 1 and go to the end of the string
print(name[1:5])     #this means start from index 1 and go to index 5 but since the string has only 5 characters it will go to the end of the string.


# to reverse the string we can use slicing with negative step
print(name[ : :-1])    #this means start from the end and go to the beginning with step -1
