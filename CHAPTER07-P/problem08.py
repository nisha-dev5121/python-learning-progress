''' for n = 3
*

**

***  '''





n = int(input("Enter the number: "))

for i in range (1, (n+1)):
   
    print("*"* (i),) 
 # now here we don't need to add [print("\n")] thing,
 # because we don't want space and star thing on the same horizontal line.
 # so that's why we didn't use the (end="") so when we didn't use that,
 # that means we didn't try to force two different lines to be together. 
 # there we had to write that cause if we didn't had it would've printed the next set of space an stars in that line only.
 
