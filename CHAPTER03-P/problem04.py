name = 'nisha is a  good  girl'
print(name.replace('  ', ' '))
# this will replace all the occurrences of double space with a single space in the string "nisha is a good girl". In this case, it will replace the double space between "a" and "good" with a single space, resulting in the string "nisha is a good girl". The replace() method takes two arguments: the first argument is the substring to be replaced, and the second argument is the substring to replace it with. In this case, we are replacing double space with a single space.    

print(name)
# this will print the original string "nisha is a  good  girl" because the replace() method does not modify the original string, it returns a new string with the replacements made. So if we want to see the changes we have to print the new string returned by the replace() method, not the original string. In this case, we are printing the original string which is "nisha is a  good  girl".
# as strings are immutable, we cannot change the original string, we can only create a new string with the changes we want to make. So if we want to see the changes we have to print the new string returned by the replace() method, not the original string. In this case, we are printing the original string which is "nisha is a  good  girl"
# original doesn't change.
# for a funtion it made a new one but the original is not changed in core