import mysql.connector as mycon

mcon = mycon.connect(host="localhost", user="root", password="root")
cursor = mcon.cursor()

# Initialize the database and tables
cursor.execute("""CREATE DATABASE IF NOT EXISTS company""")
cursor.execute("USE company")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS employee(
        empno INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        department TEXT,
        salary INTEGER
    )"""
)
mcon.commit()

print("=" * 40)
print("EMPLOYEE SEARCHING FORM")
print("-" * 40)

ans = "y"
while ans.lower() == "y":
    eno = int(input("ENTER EMPNO TO SEARCH: "))
    cursor.execute("SELECT * FROM employee WHERE empno=%s", (eno,))
    result = cursor.fetchall()

    if cursor.rowcount == 0:
        print("Sorry! Employee not found.")
    else:
        print(
            "%10s" % "EMPNO", "%20s" % "NAME", "%15s" % "DEPARTMENT", "%10s" % "SALARY"
        )

    for row in result:
        print("%10s" % row[0], "%20s" % row[1], "%15s" % row[2], "%10s" % row[3])

    ans = input("SEARCH MORE (Y): ")
