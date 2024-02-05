import os


def longest_word(file):
    text = file.read()
    words = text.split()

    n = 0
    word = ""
    for w in words:
        n += 1
        if len(w) > len(word):
            word = w
    return n, word


filename = input("Please input name of the file: ")
# Find the folder of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Form the path to the file located in this folder
file_path = os.path.join(script_dir, filename)
try:
    with open(f"{file_path}", "r") as file:
        n, word = longest_word(file)
        print(f"'{word}' is the longest word and is the word #{n} in the file")
except FileNotFoundError:
    print("Could not find the file")
