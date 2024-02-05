import os


def count_vowels(file):
    text = file.read()
    words = text.split()
    n = 0
    for w in words:
        if w[0].lower() in "aeiou":
            n += 1
    return n


filename = input("Please input name of the file: ")
# Find the folder of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Form the path to the file located in this folder
file_path = os.path.join(script_dir, filename)
try:
    with open(f"{file_path}", "r") as file:
        n = count_vowels(file)
        print(f"There are {n} words in the file that start with a vowel.")
except FileNotFoundError:
    print("Could not find the file")
