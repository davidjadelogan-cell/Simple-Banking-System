import os

def deposit(balance, amount):
    amount = float(input("Enter the amount you want to deposit: "))
    
    if amount <= 0:
        print("invalid amount")
        return 0
    else: 
        return amount


def withdraw(balance, amount):
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount > balance:
        print("insufficent funds")
        return 0
    else: 
        return amount


def get_summary(transactions):
    summary = "          Transaction Summary          \n"
    

    if len(transactions) == 0:
        
        summary += "No Transaction Was Made"
    else:
        for transaction, amount in transactions:
            summary += f"{transaction}: {amount: .2f}\n"
   
    summary += f"Current Balance: {current_balance:.2f}"
    
    return summary


transactions = []
balance = 0
amount = 0
is_running = True
current_balance = balance

while is_running: 
    print("**********************************")
    print("Welcome to Dracco Banking Systems") 
    print("**********************************")
    
    print (f"current_balance: {current_balance: .2f}")

    print("1 Deposit")
    print("2 Withdraw")
    print("3 Exit\n ")

    try:
        action = int(input("please select the action you want to perform: ")) 
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if action == 1:
        deposited = deposit(balance, 0)
        balance += deposited
        current_balance = balance
        transactions.append(("Deposit", deposited))
        

    elif action == 2:
        withdrawn = withdraw(balance, 0)
        balance -= withdrawn
        current_balance = balance
        transactions.append(("withdraw", withdrawn))
       

    elif action == 3:
        is_running = False
        print("Thank you for using Dracco Bank")
    
    else:
        print("invalid input,\n please select a valid input")

title = "summary.txt"
content = get_summary(transactions)

folder = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(folder, title)

with open (path, "w") as file:
     file.write(content)
