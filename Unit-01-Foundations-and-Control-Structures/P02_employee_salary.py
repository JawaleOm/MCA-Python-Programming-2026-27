# Python program to calculate employee salary

# Accept basic salary
basic_salary = float(input("Enter basic salary: "))

# Calculate DA (Dearness Allowance)
da = 0.10 * basic_salary

# Calculate HRA (House Rent Allowance)
hra = 0.20 * basic_salary

# Calculate gross salary
gross_salary = basic_salary + da + hra

# Calculate tax deduction
tax = 0.05 * gross_salary

# Calculate net salary
net_salary = gross_salary - tax

# Display the results
print("\n----- Employee Salary Details -----")
print("Basic Salary =", basic_salary)
print("DA =", da)
print("HRA =", hra)
print("Gross Salary =", gross_salary)
print("Tax Deduction =", tax)
print("Net Salary =", net_salary)