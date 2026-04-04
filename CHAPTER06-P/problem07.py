post = input("Enter your post about python mentors: ")

if "Harry".lower() in post.lower():
# if "harry" in post.lower():  # this also works fine


    print("This post is about Harry.")
else:
    print("This post is not about Harry.")


#If the user types "YES", "Yes", or "yEs", .lower() turns it into "yes".
#That way, your program doesn’t break just because of capitalization differences.