
# Q2: Calculate Student Marks Using *args and **kwargs

def student_result(name, *marks, **details):

    total = sum(marks)
    average = total / len(marks) if marks else 0
    highest = max(marks) if marks else 0

    print("\n----- STUDENT RESULT -----")
    print("Student Name:", name)

    # Display additional information
    for key, value in details.items():
        print(key.capitalize() + ":", value)

    print("Subject Marks:", marks)

    return total, average, highest


# Function call
total, average, highest = student_result(
    "Om Jawale",
    85, 90, 78, 92, 88,
    roll_number=101,
    student_class="MCA First Year"
)

# Display result
print("\n----- MARKS SUMMARY -----")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Highest Marks: {highest}")
