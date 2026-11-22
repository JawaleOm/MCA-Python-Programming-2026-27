# Q4: Tuples, Sets and Set Operations
roll_numbers = (101, 102, 103, 104, 105)

print("----- TUPLE OPERATIONS -----")
print("Roll numbers:", roll_numbers)
for roll in roll_numbers:
    print(roll)
print("Index 0:", roll_numbers[0])
print("Slice [1:4]:", roll_numbers[1:4])
print("Concatenation:", roll_numbers + (106, 107))

course_a = {101, 102, 103, 104}
course_b = {103, 104, 105, 106}

print("\n----- SET OPERATIONS -----")
print("Course A:", course_a)
print("Course B:", course_b)
print("Union:", course_a | course_b)
print("Intersection:", course_a & course_b)
print("Difference (A - B):", course_a - course_b)
print("Symmetric difference:", course_a ^ course_b)

combined = course_a | course_b
print("Course A subset of combined:", course_a.issubset(combined))
print("Combined superset of Course A:", combined.issuperset(course_a))

course_a.add(107)
print("After add(107):", course_a)
course_a.discard(102)
print("After discard(102):", course_a)

limit = int(input("\nGenerate squares of even numbers from 0 through: "))
even_squares = {x ** 2 for x in range(limit + 1) if x % 2 == 0}
print("Squares of even numbers:", even_squares)
