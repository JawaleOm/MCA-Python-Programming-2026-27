# 29_menu_driven.py

while True:
    print("\n----- Mathematical Application -----")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter number: "))

        if num < 2:
            print("Not a Prime Number")
        else:
            is_prime = True

            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print("Prime Number")
            else:
                print("Not a Prime Number")

    elif choice == 2:
        num = int(input("Enter number: "))

        original = num
        reverse = 0
        temp = abs(num)

        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp //= 10

        if abs(original) == reverse:
            print("Palindrome Number")
        else:
            print("Not a Palindrome Number")

    elif choice == 3:
        num = int(input("Enter number: "))

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

    elif choice == 4:
        num = int(input("Enter number: "))

        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = 1

            for i in range(1, num + 1):
                factorial *= i

            print("Factorial =", factorial)

    elif choice == 5:
        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        print("Fibonacci Series:")

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

        print()

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")