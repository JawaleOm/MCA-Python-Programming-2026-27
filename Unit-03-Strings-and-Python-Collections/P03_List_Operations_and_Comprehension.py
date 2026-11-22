# Q3: List Operations and List Comprehension
n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    numbers.append(int(input(f"Enter number {i + 1}: ")))

print("\nOriginal list:", numbers)

position = int(input("Index for insertion: "))
value = int(input("Value to insert: "))
numbers.insert(position, value)
print("After insert():", numbers)

remove_value = int(input("Value to remove: "))
if remove_value in numbers:
    numbers.remove(remove_value)
else:
    print("Value not found.")
print("After remove():", numbers)

numbers.append(int(input("Value to append: ")))
print("After append():", numbers)

numbers.extend([100, 200])
print("After extend([100, 200]):", numbers)

if numbers:
    print("Popped element:", numbers.pop())
print("After pop():", numbers)

print("\nAscending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
numbers.sort()
print("After sort():", numbers)
numbers.reverse()
print("After reverse():", numbers)

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))
else:
    print("List is empty; no maximum, minimum or sum.")

print("\nConcatenation:", numbers + [7, 8])
print("Repetition:", numbers * 2)
if numbers:
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])

search_value = int(input("Value to search: "))
print("Membership:", search_value in numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
squares = [x ** 2 for x in numbers]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Squares:", squares)
