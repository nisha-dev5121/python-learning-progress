n = int(input("Enter your number: "))

for i in range (2, n):
   if (n%i) == 0:
       print("this is not prime")
       break
else:
    print("is prime")
        
## MY MISTAKE WAS:
#i didn't use the break function so what was happening was,
#if i wrote 7, so it started to check the divisibility thing from 2
#prints the "this is not prime" then proceedes to go check for the next number then print again.
#so by using BREAK thingy it just breaks the loop and just prints it once.

#also i used BREAK function after else but that was cause the else was also under for loop,
#so if i wouldn't had wrote it then it would print the printing value lots of times.
#so by removing else from being under for loop, we don't have to write BREAK function on it.




        
## SOME IMP NOTES:
# n Python, the range() function generates a sequence of numbers starting from the first value but stopping one step before the second value.
# range(2, n) tells Python: "Start at 2 and test every number up to, but not including, n".
# If you typed in 7, range(2, 7) would only give you: 2, 3, 4, 5, and 6.

#The mathematical definition of a prime number is a number only divisible by 1 and itself.
#To prove a number is prime, you have to look for any "middle" numbers that divide it perfectly.
#If you included n in your test (by writing range(2, n + 1)), the program would eventually check if n % n == 0.
#Since every number is divisible by itself, that check would always be true,
#and your program would tell you that every single number is "not prime"
