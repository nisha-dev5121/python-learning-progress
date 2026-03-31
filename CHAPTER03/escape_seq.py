a = "nisha is a sweet girl\nand she is very kind and caring"
print(a)   #this will print the entire string as it is

name = "nisha" \
" is a sweet"      
# but if we won't give space after " then it'll just connect it with the previous word.

# it's just you gotta write in separate lines.

print(name)   #this will print the entire string as it is because we have used a backslash at the end of the first line to indicate that the string continues on the next line.






# so basically \n is used to create a new line in the string, so when we print the string it will be printed in two lines instead of one line.  
# we can obvioully use ''' to print multiple line string but this is also a way


a = "nisha is a sweet girl\tand she is very kind and caring"
print(a)   #this will print the entire string as it is but there will be a tab space between the two sentences instead of a new line.

a = "nisha is a sweet girl\\and she is very kind and caring"
print(a)   #this will print the entire string as it is but there will be a backslash between the two sentences instead of a new line or a tab space. 

a = "nisha is a sweet girl but kinda \"funny too\""
print(a)   #this will print the entire string as it is but there will be double quotes around the word "funny too" instead of a new line or a tab space.



a = 'it\'s fine'
print(a)   #this will print the entire string as it is but there will be a single quote in the word "it's" instead of a new line or a tab space.

a = "she said \"hi\""
print(a)    #this will print the entire string as it is but there will be double quotes around the word "hi" instead of a new line or a tab space.
#  how many times you wanna use single quote or dounle quote is the amount of times you gotta use \