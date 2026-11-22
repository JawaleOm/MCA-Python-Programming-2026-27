# Unit 4 - Q4(c): Python datetime Standard Library

from datetime import datetime, date

current_datetime = datetime.now()
print("Current date and time:", current_datetime)
print("Current date:", current_datetime.date())
print("Current time:", current_datetime.time())

print("\n----- DATE COMPONENTS -----")
print("Day:", current_datetime.day)
print("Month:", current_datetime.month)
print("Year:", current_datetime.year)

print("\n----- DIFFERENCE BETWEEN TWO DATES -----")
date_one_text = input("Enter first date (YYYY-MM-DD): ")
date_two_text = input("Enter second date (YYYY-MM-DD): ")

date_one = date.fromisoformat(date_one_text)
date_two = date.fromisoformat(date_two_text)

difference = abs((date_two - date_one).days)
print("Difference between dates:", difference, "days")
