d = {}


name = input("Enter friends name : ")
lang = input("Enter friends favourite language : ")
d.update({name: lang})
name = input("Enter friends name : ")
lang = input("Enter friends favourite language : ")
d.update({name: lang})
name = input("Enter friends name : ")
lang = input("Enter friends favourite language : ")
d.update({name: lang})
name = input("Enter friends name : ")
lang = input("Enter friends favourite language : ")
d.update({name: lang})

print(d)    

#it only works for unique keys.
#cause if we use this update method and suppose there are 2  people of same name,
#then the value of that key will be updated and the previous value will be lost.
#and it's about the key not the value, value can be repated but keys can't cause in dict keys are indexed so they gotta be unique.

#if the lang is same of 2 people then it's not a problem because the keys are different but if the keys are same then it's a problem because the value of that key will be updated and the previous value will be lost.