mark = int(input("Enter your marks: "))
if mark >= 90 :
    print("Your grade is Ex.")
elif mark >= 80 :
    print("Your grade is A.")
elif mark >= 70 :
    print("Your grade is B.")
elif mark >= 60 :
    print("Your grade is C.")
elif mark >= 50 :
    print("Your grade is D.")
elif mark < 50 :
    print("Your grade is F.")


# another way to write the above codw is:
mark = int(input("Enter your marks: "))
if mark >= 90 :
    grade = "Ex"
elif mark >= 80 :
    grade = "A"
elif mark >= 70 :
    grade = "B"
elif mark >= 60 :
    grade = "C"
elif mark >= 50 :
    grade = "D"
elif mark < 50 :
    grade = "F"
print("Your grade is: ", grade)