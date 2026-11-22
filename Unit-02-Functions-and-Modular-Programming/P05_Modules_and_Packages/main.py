
# P05: User-Defined Modules and Packages

# Import entire arithmetic module
import arithmetic

print("----- ARITHMETIC MODULE -----")

print("Addition:", arithmetic.add(20, 10))
print("Subtraction:", arithmetic.subtract(20, 10))
print("Multiplication:", arithmetic.multiply(20, 10))
print("Division:", arithmetic.divide(20, 10))


# Import selected functions
from arithmetic import add, multiply

print("\n----- SELECTED IMPORTS -----")

print("Addition:", add(50, 25))
print("Multiplication:", multiply(5, 4))


# Import functions from student package
from student import display_details, calculate_result

print("\n----- STUDENT DETAILS -----")

display_details("Om Jawale", 101, "MCA First Year")


print("\n----- STUDENT RESULT -----")

total, average, highest = calculate_result(
    85, 90, 78, 92, 88
)

print("Total Marks:", total)
print(f"Average Marks: {average:.2f}")
print("Highest Marks:", highest)
