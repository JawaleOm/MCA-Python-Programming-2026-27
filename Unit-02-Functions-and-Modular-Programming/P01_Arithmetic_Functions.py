
# Q1: Arithmetic Operations Using User-Defined Functions

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b


# Default argument
def calculate(a, b, operation="addition"):
    if operation == "addition":
        return add(a, b)
    elif operation == "subtraction":
        return subtract(a, b)
    elif operation == "multiplication":
        return multiply(a, b)
    elif operation == "division":
        return divide(a, b)
    else:
        return "Invalid operation"


# Positional arguments
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))

# Keyword arguments
print("Multiplication:", multiply(a=10, b=5))
print("Division:", divide(b=5, a=10))

# Default argument
print("Default Operation:", calculate(20, 10))

# Specifying operation
print("Custom Operation:", calculate(20, 10, operation="multiplication"))
