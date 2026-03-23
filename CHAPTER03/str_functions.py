name = "innisha kumari"

print(len(name))   #this will give the length of the string 
print(name.upper())   #this will convert the string to uppercase
print(name.lower())   #this will convert the string to lowercase  
print(name.capitalize())   #this will capitalize the first letter of the string
print(name.title())   #this will capitalize the first letter of each word in the string
print(name.count("i"))   #this will count the number of times the letter "i" appears in the string
print(name.find("i"))   #this will return the index of the first occurrence of the letter "i" in the string
print(name.find("a"))   #this will return -1 because the letter "z" is not in the string
print(name.replace("i", "a"))   #this will replace all occurrences of the letter "i" with the letter "a" in the string
print(name.replace("n", "m", 1))   #this will replace the first occurrence of the letter "n" with the letter "m" in the string      
print(name.replace("n", "m", 2))   #this will replace the first two occurrences of the letter "n" with the letter "m" in the string but since there is only one occurrence of the letter "n" it will replace that one occurrence and ignore the second occurrence which does not exist in the string  
print(name.endswith("ari"))   #this will return True because the string ends with "ari"
print(name.endswith("kumari"))   #this will return True because the string ends with "kumari"
print(name.startswith("Inn"))   #this will return True because the string starts with "innisha"
print(name.startswith("inn"))   #this will return True because the string starts with "innisha" 


# a = "nisha"
# a[0] = "h"
# print(a[0])

# basically this is saying that a string is assigned to a variable and if we want that a change must be done in the original string
# so that can't be done. like we can customise but by using the replace function
# so that little or the owrd of that string will be replaced by another
# but it will be valid only till that function as the original string is not changed. cause strings are immutable.



a = "nisha"
print(a[0])   #this will print the first letter of the string which is "n"
# but if we try to change the value of the first letter of the string it will give
# index means the position of that letter

#  we can use chatgpt to get ore string functions, thes e are some basic ones so no nedd to learn it all by heart just know that there are many string functions available and you can use them to manipulate strings in different ways.




# ("i","m",2) this means the first 2 occurrences of the letter "i" will be replaced by the letter "m" but since there are only 2 occurrences of the letter "i" in the string it will replace both of them and ignore the third occurrence which does not exist in the string.
# so in that bracket it means occurrence.
# but any number in [] bracket means index number. like [0] means the first letter, [1] means the second letter and so on. and [-1] means the last letter, [-2] means the second last letter and so on. and [0:3] means from index 0 to index 3 but index 3 is excluded so it will print from index 0 to index 2 only. and [1:4] means from index 1 to index 4 but index 4 is excluded so it will print from index 1 to index 3 only. and [ :3] means from the beginning of the string to index 3 but index 3 is excluded so it will print from the beginning of the string to index 2 only. and [1: ] means from index 1 to the end of the string. and [ : ] means from the beginning of the string to the end of the string which is basically the whole string. and [ : :-1] means from the end of the string to the beginning of the string with step -1 which is basically reversing the string. and [ : :-2] means from the end of the string to the beginning of the string with step -2 which is basically reversing every second letter in the string. and so on.  
