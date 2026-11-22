# Unit 4 - Q2: File Handling - Read, Write and Append

filename = "student.txt"

# Write mode creates the file or overwrites its existing contents.
file = open(filename, "w", encoding="utf-8")
try:
    print("Enter student details:")
    name = input("Student name: ")
    roll_number = input("Roll number: ")
    course = input("Course: ")

    file.write("Student Details\n")
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_number}\n")
    file.write(f"Course: {course}\n")
finally:
    file.close()

print("\nFile closed after writing:", file.closed)

# Read and display the complete file.
file = open(filename, "r", encoding="utf-8")
try:
    print("\n----- COMPLETE FILE CONTENTS -----")
    print(file.read())
finally:
    file.close()

# Append another student record without deleting existing content.
file = open(filename, "a", encoding="utf-8")
try:
    print("\nEnter another student record to append:")
    name = input("Student name: ")
    roll_number = input("Roll number: ")
    course = input("Course: ")

    file.write("\nAdditional Student Record\n")
    file.write(f"Name: {name}\n")
    file.write(f"Roll Number: {roll_number}\n")
    file.write(f"Course: {course}\n")
finally:
    file.close()

# Read the file line by line.
file = open(filename, "r", encoding="utf-8")
try:
    print("\n----- FILE CONTENTS LINE BY LINE -----")
    for line in file:
        print(line, end="")
finally:
    file.close()

# Demonstrate readlines() to display all lines as a list.
file = open(filename, "r", encoding="utf-8")
try:
    all_lines = file.readlines()
    print("\n\n----- ALL LINES USING readlines() -----")
    print(all_lines)
finally:
    file.close()

print("\nFile closed:", file.closed)
