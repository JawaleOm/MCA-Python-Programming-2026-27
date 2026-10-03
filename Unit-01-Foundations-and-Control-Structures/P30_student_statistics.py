# 30_student_statistics.py

n = int(input("Enter number of students: "))

if n <= 0:
    print("Number of students must be greater than 0.")
else:
    marks = []

    for i in range(1, n + 1):
        mark = float(input(f"Enter marks of student {i}: "))

        while mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            mark = float(input(f"Enter marks of student {i}: "))

        marks.append(mark)

    total = sum(marks)
    average = total / n
    highest = max(marks)
    lowest = min(marks)

    passed = 0
    failed = 0
    above_75 = 0

    for mark in marks:
        if mark >= 40:
            passed += 1
        else:
            failed += 1

        if mark > 75:
            above_75 += 1

    print("\n----- Class Statistics -----")
    print("Class Average =", average)
    print("Highest Marks =", highest)
    print("Lowest Marks =", lowest)
    print("Number of Passed Students =", passed)
    print("Number of Failed Students =", failed)
    print("Students Scoring Above 75% =", above_75)