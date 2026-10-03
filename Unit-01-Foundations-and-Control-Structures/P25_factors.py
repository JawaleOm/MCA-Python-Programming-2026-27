# 25_factors.py

num = int(input("Enter an integer: "))

if num == 0:
    print("Every non-zero integer is a factor of 0.")
else:
    num = abs(num)
    count = 0

    print("Factors:")

    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
            count += 1

    print("\nTotal Number of Factors =", count)