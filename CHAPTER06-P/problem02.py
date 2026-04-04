m1 = int(input("Enter the marks of subject 1: "))
m2 = int(input("Enter the marks of subject 2: "))
m3 = int(input("Enter the marks of subject 3: "))


total_percentage =100 * (m1 + m2 + m3) / 300

if total_percentage >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33 :
    print("Congratulations! You have passed the exam.", total_percentage)
else :
    print("Sorry! You have failed the exam.", total_percentage)

