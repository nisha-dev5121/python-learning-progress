# soo bascially when we used methods in string for any change 
# we had to create a new print for each change.

#  but in list just keep on doing the changes and it'll occur in the main one and use the print function just once to see it, as it is mutable.


friends = ["harsh", 87, 6.75, "apple", "rohan"]
print(friends)

friends.append("mango")  # this will add the element at the end of the list
print(friends)

l1 = [65, 98, 7,90, 56, 4]
# l1.sort()  # this will sort the list in ascending order
# l1.reverse()  # this will reverse the list
# here it has revrsed the ascending order to descending order.
# but if we had done the reverse first and then sort it, it would have sorted in ascending order only, as the sort method will override the reverse method.

# l1.insert(4,448)  # this will insert the element at the specified index, in this case it will insert 448 at index 4 and shift the rest of the elements to the right.    
# l1.pop(4)  # this will remove the element at the specified index, in this case it will remove the element at index 4 which is 56 and shift the rest of the elements to the left.
print(l1.pop(4))  # this will return the element that is removed, in this case it will return 56.    
print(l1)



# as we can see that after applying function to the lists
# and at the end saying just to print the list and not specifying to print the function version
# it's printing the function version only cause a function changes the orginal list to the core and not just for that function as we saw in strings that it was not changing the original string but just for that function.


l1.remove(90)  # this will remove the first occurrence of the specified element, in this case it will remove 90 from the list.
print(l1)