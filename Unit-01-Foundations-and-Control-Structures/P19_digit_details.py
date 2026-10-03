# 19_digit_details.py

num = int(input("Enter an integer: "))

num = abs(num)

if num == 0:
    count = 1
    largest = 0
    smallest = 0
else:
    count = 0
    largest = 0
    smallest = 9

    while num > 0:
        digit = num % 10

        count += 1

        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

        num //= 10

print("Number of Digits =", count)
print("Largest Digit =", largest)
print("Smallest Digit =", smallest)