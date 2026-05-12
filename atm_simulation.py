# Project Title: ATM Simulation 
# Create a menu-driven Python program that simulates an ATM with the 
# following options: 
# 1. Check Balance 
# 2. Deposit Money 
# 3. Withdraw Money 
# 4. Exit 
# The program should use loops, conditional statements, and user input. 


def deposit_money(balance):
    try:
        amount = int(input("Enter amount (in digits): "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return balance
    if amount > 0:
        balance += amount
        print(amount,"credited to your account.")
    else:
        print("Invalid input")
    return balance

def withdraw_money(balance):
    try:
        amount = int(input("Enter amount (in digits): "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return balance
    if amount > 0 and amount <= balance : 
        balance -= amount
        print(amount,"debited to your account.")
    elif amount > balance:
        print("insufficient balance!")
    else:
        print("Invalid input")
    return balance

balance = 1000
pin = None
while pin is None:
    try:
        pin = int(input("Enter your pin:"))
    except ValueError:
        print("Error: Please enter a valid number.")
count = 0

while True:
    count += 1
    if pin == 1234:
        print("1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit ")
        option = int(input("Enter your choice:"))

        match option:
            case 1:
                print("Current balance:", balance)
            case 2:
                balance = deposit_money(balance)
            case 3:
                balance = withdraw_money(balance)
            case 4:
                print("Goodbye!")
                break
            case _:
                print("Invalid input")
    elif count == 3:
        print("Your debit card is blocked!")
        exit()
    else:
        print("Incorrect pin!")
        pin = int(input("Please enter valid pin:"))