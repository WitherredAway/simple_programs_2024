"""Program to manage a database of students using MySql"""


import time
import mysql.connector as mcon

con = mcon.connect(host="localhost", user="root", passwd="root")
cursor = con.cursor(dictionary=True)

# Initialize the database and tables
cursor.execute("""CREATE DATABASE IF NOT EXISTS students""")
cursor.execute("USE students")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        class INTEGER,
        section TEXT
    )"""
)

con.commit()


BORDER = "-" * 30


def format_dict(dictionary, *, indent="  "):
    """Function to nicely format the keys and values of a dictionary"""

    # This list comprehension is used to format each key and value of the dictionary
    return "\n".join(
        [
            f"{indent}{key.title() if isinstance(key, str) else key}: {value}"
            for key, value in dictionary.items()
        ]
    )


def execute(query, params=None):
    """Function to execute SQL queries on the database and automatically commit.

    Returns cursor.rowcount"""

    cursor.execute(query, params)
    if cursor.rowcount:
        con.commit()
    return cursor.rowcount


def add_student(name, _class, section):
    """Adds a student's details to the database and returns the inserted ID"""

    execute(
        """INSERT INTO students (name, class, section)
        VALUES (%(name)s, %(class)s, %(section)s)""",
        {"name": name, "class": _class, "section": section},
    )
    return cursor.lastrowid


def get_students(_id=None, *, n=None):
    """Returns details of student with given ID or all students"""

    params = []
    if _id is None:
        query = "SELECT * FROM students"
    else:
        query = "SELECT * FROM students WHERE id = %s"
        params.append(_id)

    execute(query, params)
    return cursor.fetchall() if n is None else cursor.fetchmany(n)


def remove_student(_id):
    """Removes an entry from the students table"""

    rowcount = execute("""DELETE FROM students WHERE id = %s""", (_id,))
    return rowcount


data = {}
while True:
    time.sleep(1)
    option = input(
        f"""
{BORDER}
1. Add Student Data
2. View Student Data
3. Remove Student Data
{BORDER}
Please choose an option: """
    )

    try:
        option = int(option)
    except ValueError:
        con.close()
        break

    if option == 1:
        name = input("Name: ")

        while True:
            try:
                _class = int(input("Class: "))
            except ValueError:
                print("Class must be an integer")
                continue
            else:
                break

        section = input("Section: ")

        _id = add_student(name, _class, section)
        print(f"Added student #{_id} to database.")

    elif option == 2:
        _id = input("Please input ID of student to view. Leave empty to view all: ")

        if len(_id) == 0:
            students = get_students()
            for std in students:
                print(format_dict(std))
                print()
        else:
            _id = int(_id)
            student_data = get_students(_id)
            if not student_data:
                print("Student does not exist in database.")
                continue
            print(format_dict(student_data))

    elif option == 3:
        _id = int(input("Please input ID of student to remove: "))

        success = remove_student(_id)
        if success:
            print(f"Deleted student #{_id} from database.")
        else:
            print("Student does not exist in database.")
