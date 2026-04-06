# the break statement is used to exit a loop prematurely,
# while the continue statement is used to skip the current iteration of a loop and move on to the next one.


#break statement example
for i in range (80):
    if i ==8:
        break
    print(i)
#when it reached 8 the loop broke.
#if we don't write the range as (1,80) and rather just,
#(80) so it will start from 0.



#continue statement example
for i in range (10):
    if i == 5:
        continue
    print(i)
    #skipped 5, and continued.



for i in range (4):
    print("printing")
    if i == 2:
        continue
    print(i)
    #when i is 2, it will skip the print statement and continue to the next iteration of the loop. So it will not print 2, but it will print 0,1,3. 
    #output will be:
    #printing       
    #0
    #printing
    #1
    #printing
    #printing
    #3
    