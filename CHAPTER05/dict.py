marks = {
    "Harry": 98,
    "Nisha": 100,
    "Rohan": 43,
}

# print(marks, type(marks))
# dictionary is used if we want that certain key values be stuck with certain values and in list form.
# like here nisha key value has 100 as her value with others in the list.

# so basically a dictionary is a list of key value pairs



# print(marks["Nisha"])

# so here we don't have index value assigned to names,
# we can just write the key value to get the paired key value.
# this is useful cause if there were a list of 10000 students, we can just easily look up the name 
# and it will show us it's corresponding marks.
# or write the mark key value and get the names attchted to it.


print(marks["100"])


# dicts are mutable, and they should not have duplicate keys for different values in them.
# the keys are indexed. soo if we want nisha marks it wpon't look in the list one by one to search nisha, cause nisha is indexed.