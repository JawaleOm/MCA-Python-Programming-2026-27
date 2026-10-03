# 13_atm.py

correct_pin = 1234

pin = int(input("Enter PIN: "))

if pin != correct_pin:
    print("Invalid PIN")
else:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid withdrawal amount")
    elif amount > balance:
        print("Insufficient Balance")
    elif amount % 100 != 0:
        print("Amount must be a multiple of 100")
    else:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)