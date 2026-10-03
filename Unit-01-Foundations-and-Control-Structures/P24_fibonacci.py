# 24_fibonacci.py

n = int(input("Enter number of terms: "))

a = 0
b = 1
total = 0

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    total += a

    a, b = b, a + b

print("\nSum =", total)