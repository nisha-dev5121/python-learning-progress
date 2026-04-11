''' for n= 3 as in total 3 spaces for the pattern

  *     #2 spaces
 ***    #1 space
***** 

## so basically if n=3 then the first number of space given will be 2 (one less than given value of n) '''



# so before writing this end thing what was happening was:
# after getting the user inpu let's say user said n = 3,
# so by the program this is what happenes line by line:

'''
     # space of 2 was left
*    # now instaed of printing the star next to the space it printed it on the next line.
     # space of 1 was left
***  # again same thing
     # here no space was left as here (n-i) would be 0 but it looks like space was left cause print didn't print anything as given.
*****'''
# now as python code runs line by line so what was happining that the space code worked on one line then to prit the star it went to the next line as given it to be,
# that's why we used (end="") so what is does is it doesn't let the code run to the next line and excute the nrxt orint value beside it.


n = int(input("Enter the number: "))



for i in range (1, (n+1)):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="") # to get odd numbers this is used, to get even we use (2n) or here (2i)
    print("")


#The print("\n"): 
# This is your manual "Enter" key. 
# Once a row of spaces and stars is finished, this moves the cursor to the next line to begin the next row.

#Note: Since print() adds a newline by default,
#this code print("\n") actually adds two newlines, which will put a blank gap between every row of the pyramid. 
# A simple print() with nothing inside is the standard way to just move down one line.

# to not have 2 newlines we will just use print("") and not print("\n")