import sqlite3

name = "C-jay H. Santos"
program = "BSIS 4-A"

with sqlite3.connect("students.db") as conn:
    conn.execute(
        "INSERT INTO students (name, program) VALUES (?, ?)",
        (name, program)
    )

print("Student saved")