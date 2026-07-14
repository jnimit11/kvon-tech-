import os 
from config import FILE_PATH, ENCODING

def append_to_file(file_path, content):

    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist.")
    
    with open(file_path, "a", encoding=ENCODING) as file:
        file.write("\n" + content)

try:
    print("file Path:", FILE_PATH)
    print("file exists :", FILE_PATH.exists())

    new_content = input("ENter text to append: ")

    append_to_file(FILE_PATH, new_content)
    print("\nContent appended successfully.")

except FileNotFoundError as e:
    print("Error", e)
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("\nProgram Finished.")

    