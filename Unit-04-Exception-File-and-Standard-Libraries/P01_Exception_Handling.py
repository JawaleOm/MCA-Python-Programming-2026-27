# Unit 4 - Q1: Exception Handling

print("----- DIVISION WITH EXCEPTION HANDLING -----")
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ValueError:
    print("Error: Please enter valid numerical values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division result:", result)
finally:
    print("Division operation completed.")


print("\n----- LIST INDEX HANDLING -----")
sample_list = [10, 20, 30, 40]
try:
    index = int(input("Enter a list index (0 to 3): "))
    print("Element:", sample_list[index])
except ValueError:
    print("Error: Index must be an integer.")
except IndexError:
    print("Error: List index is out of range.")
else:
    print("List access completed successfully.")
finally:
    print("List operation completed.")


print("\n----- AGE VALIDATION USING RAISE -----")
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
except ValueError as error:
    print("Error:", error)
else:
    print("You are eligible.")
finally:
    print("Age validation completed.")
