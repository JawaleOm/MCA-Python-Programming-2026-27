# Python program to calculate electricity bill
# according to different consumption slabs

# Accept number of units consumed
units = float(input("Enter electricity units consumed: "))

# Calculate electricity bill
if units <= 100:
    bill = units * 1.50

elif units <= 200:
    bill = (100 * 1.50) + ((units - 100) * 2.50)

elif units <= 300:
    bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

else:
    bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 6.00)

# Display the result
print("\n----- Electricity Bill -----")
print("Units Consumed =", units)
print("Electricity Bill = ₹", bill)