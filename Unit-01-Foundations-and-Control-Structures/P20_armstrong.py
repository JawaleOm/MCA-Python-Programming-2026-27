# 20_armstrong.py

num = int(input("Enter an integer: "))

if num < 0:
    print("Not an Armstrong Number")
else:
    original = num
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == original:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")