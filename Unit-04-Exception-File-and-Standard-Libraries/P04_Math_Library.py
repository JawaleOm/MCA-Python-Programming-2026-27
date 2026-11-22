# Unit 4 - Q4(a): Python math Standard Library

import math

number = float(input("Enter a non-negative number: "))
factorial_number = int(input("Enter a non-negative integer for factorial: "))
power_value = float(input("Enter power value: "))

if number < 0:
    print("Square root is not defined for a negative real number.")
else:
    print("Square root:", math.sqrt(number))

if factorial_number < 0:
    print("Factorial is not defined for negative integers.")
else:
    print("Factorial:", math.factorial(factorial_number))

print("Power:", math.pow(number, power_value))
print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))
