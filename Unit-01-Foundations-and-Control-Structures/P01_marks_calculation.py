# Python program to calculate total marks, average marks, and percentage

# Accept marks for five subjects
marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))

# Calculate total marks
total = marks1 + marks2 + marks3 + marks4 + marks5

# Calculate average marks
average = total / 5

# Calculate percentage
# Assuming each subject is out of 100
percentage = (total / 500) * 100

# Display the results
print("\n----- Result -----")
print("Total Marks =", total)
print("Average Marks =", average)
print("Percentage =", percentage, "%")