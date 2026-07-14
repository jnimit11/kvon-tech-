import os
import string
from config import FILE_PATH, ENCODING


def count_words(file_path):

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError("File does not exist.")

    # Check if file is empty
    if os.path.getsize(file_path) == 0:
        raise ValueError("File is empty.")

    word_count = {}

    # Open file safely
    with open(file_path, "r", encoding=ENCODING) as file:

        # Read file line by line
        for line in file:

            # Convert to lowercase and split into words
            words = line.lower().split()

            for word in words:

                # Remove punctuation
                word = word.strip(string.punctuation)

                if word:
                    word_count[word] = word_count.get(word, 0) + 1

    return word_count


# ---------------- Main Program ---------------- #

try:

    print("File Path :", FILE_PATH)
    print("File Exists :", FILE_PATH.exists())

    result = count_words(FILE_PATH)

    print("\nWord Frequency\n")

    for word, count in result.items():
        print(f"{word} : {count}")

except FileNotFoundError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("\nProgram Finished.")