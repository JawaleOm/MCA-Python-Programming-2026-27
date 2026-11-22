# Unit 4 - Q4(b): Python random Standard Library

import random

print("Random integer between 1 and 100:", random.randint(1, 100))

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("\nOriginal list:", fruits)

print("Randomly selected fruit:", random.choice(fruits))

random.shuffle(fruits)
print("List after shuffle:", fruits)
