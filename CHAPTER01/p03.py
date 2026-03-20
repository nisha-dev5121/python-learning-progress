import os

# Specify the directory path you want to list
# Use '.' for the current working directory
directory_path = '.'

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)

# this bacially lists all the files and directories in the specified directory path