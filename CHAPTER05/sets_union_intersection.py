s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}

print(s1.union(s2))
#union method is used to get the union of two sets, it will return a new set that contains all the unique elements from both sets.
#here we are getting the union of s1 and s2, so it will return a new set that contains all the unique elements from both sets, which is {1, 45, 6, 7, 8, 78}.   

print(s1.intersection(s2))
#intersection method is used to get the intersection of two sets, it will return a new set that contains only the common elements from both sets.
#here we are getting the intersection of s1 and s2, so it will return a new set that contains only the common elements from both sets, which is {1}.    

print(s1.difference(s2))
#difference method is used to get the difference of two sets, it will return a new set that contains only the elements that are present in the first set but not in the second set.
#here we are getting the difference of s1 and s2, so it will return a new set that contains only the elements that are present in s1 but not in s2, which is {45, 6}.

print({1, 2}.issubset(s2))
#issubset method is used to check if a set is a subset of another set, it will return True if the set is a subset of another set, otherwise it will return False.
#here we are checking if the set {1, 2} is a subset of the set s2, so it will return False because the set {1, 2} is not a subset of the set s2.
