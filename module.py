import pyjokes

# prints a random joke
joke=pyjokes.get_joke()
print(joke)
# You are making progress if each mistake is a new one.

import os

# Ask the user to input a directory path
directory_path = input("Enter the path of the directory: ") #C:\\Users\\ADMIN\\Documents

# Check if the path exists and is a directory
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print(f"\nContents of '{directory_path}':")
    contents = os.listdir(directory_path)  # List files and directories
    for item in contents:
        print(item)
else:
    print("Invalid directory path.")
