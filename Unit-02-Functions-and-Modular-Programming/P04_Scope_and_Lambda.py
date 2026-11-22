
# Q4: Scope, Lifetime and Lambda Functions

# Global variable
counter = 10

def demonstrate_scope():
    global counter

    # Local variable
    local_message = "I am a local variable"

    print("Inside function - global counter:", counter)
    print("Inside function - local message:", local_message)

    # Modifying global variable
    counter += 5

    # Local variable
    temporary_value = 100
    print("Temporary local value:", temporary_value)


# Calling function
demonstrate_scope()

print("Outside function - updated global counter:", counter)

# Lambda functions
square = lambda x: x * x
cube = lambda x: x ** 3
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

# Display results
print("\n----- LAMBDA FUNCTIONS -----")
print("Square of 5:", square(5))
print("Cube of 3:", cube(3))
print("Maximum of 10 and 20:", maximum(10, 20))
print("Addition of 15 and 25:", addition(15, 25))
