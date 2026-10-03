# 10_number_check.py

num = int(input("Enter an integer: "))

if num == 0:
    print("The number is Zero")
elif num > 0:
    print("The number is Positive")

    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
else:
    print("The number is Negative")

    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")