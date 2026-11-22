# Unit 4 - Q5: Command-Line Arguments
# Usage:
# python P05_Command_Line_Arguments.py 20 10 +
# python P05_Command_Line_Arguments.py 20 10 "*"

import sys

if len(sys.argv) != 4:
    print("Usage: python P05_Command_Line_Arguments.py <number1> <number2> <operator>")
    print('Example: python P05_Command_Line_Arguments.py 20 10 "+"')
    sys.exit(1)

try:
    number1 = float(sys.argv[1])
    number2 = float(sys.argv[2])
except ValueError:
    print("Error: The first two arguments must be numbers.")
    sys.exit(1)

operator = sys.argv[3]

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 == 0:
        print("Error: Division by zero is not allowed.")
        sys.exit(1)
    result = number1 / number2
else:
    print("Error: Invalid operator. Use +, -, * or /.")
    sys.exit(1)

print(f"Result: {number1} {operator} {number2} = {result}")
