# 17_palindrome.py

num = int(input("Enter an integer: "))

original = num
num = abs(num)
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if abs(original) == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")