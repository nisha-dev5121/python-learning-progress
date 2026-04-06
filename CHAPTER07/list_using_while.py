l = [1, 7, "Nisha", "Shivam", 33.14, "Harry", "Harsh"]

i = 0
while (i < len(l)):
    print(l[i])
    i += 1
# this will print all the elements of the list one by one.
# Output:
# 1
# 7
# Nisha
# Shivam
# 33.14
# Harry
# Harsh
# as you can see that we have used the len() function to get the length of the list and then we have used that length in the condition of the while loop to print all the elements of the list one by one.


# we took i = 0 so now as 0 is less than the length of the list here (as length of the list here is 7) so it will print the element at index 0 that is 1 and then it will go to the next line which says i = i + 1 so now i will become 1 and as this is a loop so it will again check the condition and as in this case as well i (that is 1 now) and is also less than the length of the list (that is 7) so now it will print the element at index 1 that is 7 and now it will continue till the condition is proved false that is when i will become 7 here.)
#now then it will print the 0 indexed value.
#and will kwwp on printing the values till we reach i value of 7 as it will be not less than the length of the list.
#and we made condition like that obviously because if we make condition like i < 6 then it will not print the last element of the list that is "Harsh" as it is at index 6 and if we make condition like i <= 6 then it will give an error as there is no element at index 7 in the list.