# Q1: String Operations and String Methods
sentence = input("Enter a sentence: ")

print("\n----- BASIC STRING OPERATIONS -----")
print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Trimmed:", sentence.strip())

old_word = input("Word to replace: ")
new_word = input("Replacement word: ")
print("After replacement:", sentence.replace(old_word, new_word))

character = input("Character to count: ")
if len(character) == 1:
    print("Occurrences:", sentence.count(character))
else:
    print("Enter exactly one character.")

start_text = input("Substring to check at start: ")
end_text = input("Substring to check at end: ")
print("Starts with:", sentence.startswith(start_text))
print("Ends with:", sentence.endswith(end_text))

print("\n----- STRING OPERATORS -----")
first = input("First text: ")
second = input("Second text: ")
print("Concatenation:", first + " " + second)

repeat_text = input("Text to repeat: ")
repeat_count = int(input("Repetition count: "))
print("Repetition:", repeat_text * repeat_count)

search_text = input("Text to search in original sentence: ")
print("Membership:", search_text in sentence)
