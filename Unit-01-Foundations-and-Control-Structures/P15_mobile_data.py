# 15_mobile_data.py

data = float(input("Enter monthly data usage in GB: "))

if data <= 1:
    bill = 100
elif data <= 5:
    bill = 100 + (data - 1) * 50
elif data <= 10:
    bill = 300 + (data - 5) * 40
else:
    bill = 500 + (data - 10) * 30

print("Data Usage =", data, "GB")
print("Total Bill =", bill)