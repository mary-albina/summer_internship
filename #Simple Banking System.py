#Simple Banking System
def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("₹", amount, "deposited successfully.")
    else:
        print("Invalid amount.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("₹", amount, "withdrawn successfully.")
    return balance

def check_balance(balance):
    print("Current Balance: ₹", balance)

def account_details(name, acc_no, balance):
    print("\n----- ACCOUNT DETAILS -----")
    print("Account Holder:", name)
    print("Account Number:", acc_no)
    print("Balance: ₹", balance)

print("===== BANK ACCOUNT CREATION =====")
name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")
balance = float(input("Enter Initial Deposit Amount: "))

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        balance = deposit(balance)
    elif choice == 2:
        balance = withdraw(balance)
    elif choice == 3:
        check_balance(balance)
    elif choice == 4:
        account_details(name, acc_no, balance)
    elif choice == 5:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Try again.")