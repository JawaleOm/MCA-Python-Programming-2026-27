# Q5: Dictionaries, Dictionary Comprehension and Nested Collections
employee = {
    "employee_id": 101,
    "name": "Om Jawale",
    "department": "IT",
    "salary": 45000
}

print("----- EMPLOYEE INFORMATION -----")
print("Original dictionary:", employee)

employee["designation"] = "Python Developer"  # Add
employee["salary"] = 55000                     # Update
print("After adding and updating:", employee)

print("\nKeys:", employee.keys())
print("Values:", employee.values())
print("Key-value pairs:")
for key, value in employee.items():
    print(key, ":", value)

search_id = int(input("\nEnter employee ID to search: "))
if employee.get("employee_id") == search_id:
    print("Employee found:", employee)
else:
    print("Employee not found.")

deleted = employee.pop("designation", None)  # Delete
print("Deleted designation:", deleted)
print("After deletion:", employee)

# Nested dictionary containing multiple employee records
employees = {
    101: {"name": "Om Jawale", "department": "IT", "salary": 55000},
    102: {"name": "Aarav Patil", "department": "HR", "salary": 35000},
    103: {"name": "Neha Sharma", "department": "IT", "salary": 65000},
    104: {"name": "Riya Deshmukh", "department": "Finance", "salary": 40000}
}

print("\n----- ALL EMPLOYEES -----")
for emp_id, details in employees.items():
    print(emp_id, ":", details)

salary_limit = int(input("\nEnter minimum salary threshold: "))
high_salary_employees = {
    emp_id: details for emp_id, details in employees.items()
    if details["salary"] > salary_limit
}

print("\nEmployees earning above", salary_limit, ":")
for emp_id, details in high_salary_employees.items():
    print(emp_id, ":", details)
