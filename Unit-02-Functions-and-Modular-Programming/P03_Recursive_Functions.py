
# Q3: Factorial and Fibonacci Using Recursive Functions

# Recursive function for factorial
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Recursive function for Fibonacci series
def fibonacci(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    series = fibonacci(n - 1)
    series.append(series[-1] + series[-2])

    return series


# Main program
number = int(input("Enter a number for factorial: "))
terms = int(input("Enter number of Fibonacci terms: "))

print("Factorial:", factorial(number))
print("Fibonacci Series:", *fibonacci(terms))
