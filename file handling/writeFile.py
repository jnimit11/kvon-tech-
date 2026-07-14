import os 
filename = "file handling/input.txt"

if os.path.exists(filename):
    print("file exists, appending content...")
else:
    print("file do not exists")

with open(filename, "a") as file:
    file.write(" \n Hello, World!\n")
file.close()