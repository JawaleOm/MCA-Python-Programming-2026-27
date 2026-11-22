# Q2: String Slicing and String Formatting
full_name = input("Enter student's full name: ").strip()
email = input("Enter email address: ").strip()
mobile = input("Enter mobile number: ").strip()

name_parts = full_name.split()
first_name = name_parts[0] if name_parts else ""
last_name = name_parts[-1] if len(name_parts) >= 2 else ""

reversed_name = full_name[::-1]

if "@" in email:
    username, domain = email.split("@", 1)
else:
    username, domain = email, "Invalid email address"

last_four_digits = mobile[-4:]

print("\n----- STUDENT INFORMATION -----")
print("First Name:", first_name)
print("Last Name:", last_name)
print("Reversed Name:", reversed_name)
print("Email Username:", username)
print("Email Domain:", domain)
print("Last Four Mobile Digits:", last_four_digits)

print("\n----- INDEXING -----")
print("First character (index 0):", full_name[0] if full_name else "Empty name")
print("Last character (index -1):", full_name[-1] if full_name else "Empty name")

print("\n----- STRING FORMATTING -----")
print(f"Student Name: {full_name}")
print("Student Email: {}".format(email))
print("Student Mobile: %s" % mobile)
