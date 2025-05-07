current_account_number = None


def create_account():
    acc_no = input("Enter new account number: ")
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))
    while True:
        pin = input("Enter 4-digit pin: ")
        if pin.isdigit() and len(pin) == 4:
            break
        else:
            print("Invalid pin, please enter exactly 4 digits.")
    
    with open("accounts.txt", "a") as f:
        f.write(f"{acc_no},{name},{pin},{balance}\n")
    print("Account created.")


def login():
    global current_account_number  
    print("-----LOGIN-----")
    acc_no1 = input("Enter account number to login: ")
    pin1 = input("Enter pin number: ")
    found = False

    with open("accounts.txt", "r") as f:
        for line in f:
            acc_no, name, pin, balance = line.strip().split(",")
            if acc_no1 == acc_no and pin1 == pin:
                print(f"Welcome {name}!")
                current_account_number = acc_no  
                found = True
                break
    if not found:
        print("Login failed, incorrect account number or pin!")


def deposit():
    if current_account_number is None:
        print("Please log in first.")
        return

    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    updated_lines = []
    found = False

    with open("accounts.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            acc_no, name, pin, balance = line.strip().split(",")
            if acc_no == current_account_number:
                new_balance = float(balance) + amount
                updated_lines.append(f"{acc_no},{name},{pin},{new_balance}\n")
                found = True
            else:
                updated_lines.append(line)

    if found:
        with open("accounts.txt", "w") as f:
            f.writelines(updated_lines)

       
        with open("transaction.txt", "a") as t:
            t.write(f"{current_account_number}, deposit, {amount}\n")

        print("Deposit successful.")
    else:
        print("Account not found.")


def withdraw():
    if current_account_number is None:
        print("Please log in first.")
        return

    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    updated_lines = []
    found = False

    with open("accounts.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            acc_no, name, pin, balance = line.strip().split(",")
            if acc_no == current_account_number:
                current_balance = float(balance)
                if amount > current_balance:
                    print("Insufficient balance!")
                    return
                new_balance = current_balance - amount
                updated_lines.append(f"{acc_no},{name},{pin},{new_balance}\n")
                found = True
            else:
                updated_lines.append(line)

    if found:
        with open("accounts.txt", "w") as f:
            f.writelines(updated_lines)

      
        with open("transaction.txt", "a") as t:
            t.write(f"{current_account_number}, withdraw, {amount}\n")

        print("Withdrawal successful.")
    else:
        print("Account not found.")


def check_balance():
    if current_account_number is None:
        print("Please log in first.")
        return

    with open("accounts.txt", "r") as f:
        for line in f:
            acc_no, name, pin, balance = line.strip().split(",")
            if acc_no == current_account_number:
                print(f"Current balance: {balance}")
                return
    print("Account not found.")


def transaction_history():
    if current_account_number is None:
        print("Please log in first.")
        return

    print("Transaction:")
    with open("transaction.txt", "r") as t:
        for line in t:
            account_number, transaction_type, amount = line.strip().split(", ")
            if account_number == current_account_number:
                print(f"{transaction_type}: {amount}")


def menu():
    while True:
        print("\n-----MENU-----")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose: ")
        
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")



create_account()
login()
menu()
