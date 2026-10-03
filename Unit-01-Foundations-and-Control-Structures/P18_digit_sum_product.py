# 18_digit_sum_product.py

num = int(input("Enter an integer: "))

num = abs(num)
sum_digits = 0
product_digits = 1

if num == 0:
    product_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    product_digits *= digit
    num //= 10

print("Sum of Digits =", sum_digits)
print("Product of Digits =", product_digits)