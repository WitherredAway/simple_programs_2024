import csv
import os

COLUMNS = ["ID", "Name", "Author", "Year"]


def add_book(file, existing_rows, *, name, author, year):
    """Add a book to the csv"""

    _id = len(existing_rows)

    rows = existing_rows
    if not rows:
        rows.append(COLUMNS)
        _id += 1

    rows.append([_id, name, author, year])

    writer = csv.writer(file)
    writer.writerows(rows)
    return _id


name = input("Enter the name of the book: ")
author = input("Enter the name of the author: ")
try:
    year = int(input("Enter the year of publication: "))
except ValueError:
    print("Year must be an integer")
    quit()

FILENAME = "books.csv"
# Find the folder of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Form the path to the file located in this folder
file_path = os.path.join(script_dir, FILENAME)

with open(file_path, "a+") as file:
    rows = list(csv.reader(file))

with open(file_path, "w") as file:
    _id = add_book(file, rows, name=name, author=author, year=year)
    print(f"Added book with ID {_id}.")
    print()

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)
    print("All books currently in inventory:")
    for row in reader:
        print(" | ".join(row))
