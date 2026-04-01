d = {} #empty dictionary
print(d, type(d))


marks = {
    "Harry": 98,
    "Nisha": 100,
    "Rohan": 43,
}

#print(marks.items( ))
#prints the key value pairs in the form of list of tuples.
#like ([('Harry', 98), ('Nisha', 100), ('Rohan', 43)])

#print(marks.keys( ))
#prints the keys in the form of list.
#like dict_keys(['Harry', 'Nisha', 'Rohan'])

#print(marks.values( ))
#prints the values in the form of list.     
#like dict_values([98, 100, 43])

#marks.update({"Rohan": 45, "Renuka": 97})
#update method is used to update the value of a key in the dictionary.  
#print(marks)
#this happens cause dictionary is mutuable that's why when we tried to change it we didn't get an error and it updated the value of Rohan from 43 to 45. 
#and we diddn't had to write print(marks.pdate) but just print(marks) as it updates the orginal thing and we can see the change in the original thing.
#rohan mark got changed and renuka key got added.


#print(marks.get("Rohan"))
#get method is used to get the value of a key in the dictionary.

#print(marks.get("Renuka"))
#get method is used to get the value of a key in the dictionary.
#here we get none cause there is no key named renuka in the dictionary, so it returns none.
#cause the updated thing was later just added as a comment and not a command.


#print(marks["Nisha"])
#print(marks.get("Nisha"))
#both of these will give us the same output as 100, but the difference is that if we try to get a key value that is not present in the dictionary, then the first one will give us an error while the second one will give us none.

#for example
#print(marks.get("Renuka"))
#this will give us none cause there is no key named renuka in the dictionary, so it returns none.
#print(marks["Renuka"])
#this will give us an error cause there is no key named renuka in the dictionary, so it will give us a key error.

#print(marks.clear( ))
#clear method is used to clear the dictionary, it will remove all the key value pairs from the dictionary and make it empty.

#print(marks.copy( ))
#copy method is used to create a copy of the dictionary, it will return a new dictionary with the same key value pairs as the original dictionary. 

#print(marks.pop("Rohan"))
#pop method is used to remove a key value pair from the dictionary, it will return the value of the key that is removed from the dictionary.
#here we are removing the key value pair of rohan and it will return the value of rohan which is 43 and it will remove the key value pair of rohan from the dictionary.       
# after this command the dictionary will be {'Harry': 98, 'Nisha': 100} and rohan key value pair will be removed from the dictionary.   
# if we try to pop a key that is not present in the dictionary, then it will give us an error.  
 

#so basiclly with marks.pop it deletes the key and the value but it return the value of the key just ioncase if we want to use it laterr, with other varaible
# but popitem method deletes the latest added key and it's value and it doesn't return anything, it just deletes the latest added key and it's value.   

print(marks.popitem( ))
#popitem method is used to remove the latest added key value pair from the dictionary, it will remove the latest added key value pair from the dictionary and it doesn't return anything, it just deletes the latest added key value pair from the dictionary.

