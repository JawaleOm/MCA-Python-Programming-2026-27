# 11_loan_eligibility.py

age = int(input("Enter age: "))
monthly_income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

if age >= 21 and age <= 60 and monthly_income >= 25000 and credit_score >= 700:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")