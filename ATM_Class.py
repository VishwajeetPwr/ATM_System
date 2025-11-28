import json
import os

try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # Fallback for environments where __file__ is not defined
    SCRIPT_DIR = os.getcwd()

DB_PATH = os.path.join(SCRIPT_DIR, "ATM_Database.json")

from Account_Class import Account, Saving_Accounts

class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_user = None
        self.load_data()

    def save_data(self):
        data = {}
        for name, account_obj in self.accounts.items():
            data[name] = account_obj.to_dict()

        try:
            with open(DB_PATH, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            if os.path.exists(DB_PATH):
                with open(DB_PATH, "r") as f:
                    data = json.load(f)

                for name, info in data.items():
                    # 1. Extract History (or None if it's a new file)
                    history_data = info.get("history", None)
                    
                    # 2. Factory Logic (Standard vs Savings)
                    if info.get("type") == "Savings":
                        recreated_acc = Saving_Accounts(
                            info['name'], 
                            info['pin'], 
                            info['balance'], 
                            history=history_data # Pass history to constructor
                        )
                    else:
                        recreated_acc = Account(
                            info['name'], 
                            info['pin'], 
                            info['balance'],
                            history=history_data # Pass history to constructor
                        )
                    self.accounts[name] = recreated_acc
        except (FileNotFoundError, json.JSONDecodeError):
            # File doesn't exist on first run. That's okay.
            self.accounts = {}

    def create_account(self, name, pin, balance,account_type="Standard"):
        if name in self.accounts:
            print("Account already exists.")
            return
        if account_type == 'Savings':
            new_account = Saving_Accounts(name,pin,balance)
        else:
            new_account = Account(name, pin, balance)
        self.accounts[name] = new_account
        self.save_data()
        print(f"{account_type} Account created for {name} with balance {balance}")

    def login(self, name, pin):
        if name in self.accounts:
            if self.accounts[name].pin == pin:
                self.current_user = self.accounts[name]
                print(f"Login successful. Welcome, {name}!")
                return True
            else:
                print("Error: Incorrect PIN.")
        else:
            print("Incorrect Name.")

    def logout(self):
        if self.current_user:
            print(f"Goodbye, {self.current_user.name}!")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def run(self):
        print("===ATM System Started===")
        print(f"Database Location: {DB_PATH}")
        while True:

            if self.current_user is None:
                print("\n1. Create Account")
                print("2. Login")
                print("3. Logout")
                Action = input("What would you like to do? ")

                match Action:
                    case "1":
                        n = input("Enter your name: ").strip().title()
                        try:
                            p = int(input("Enter PIN: "))
                            b = int(input("Initial Balance: "))
                            print("Account Type: ")
                            print("1. Standard")
                            print("2. Savings(5% Interest)")
                            type_choice = input("Select type: ")
                            if type_choice == '2':
                                self.create_account(n,p,b,"Savings")
                            else:
                                self.create_account(n,p,b,"Standard")
                        except ValueError:
                            print("Error: PIN and Balance must be numbers.")

                    case "2":
                        n = input("Enter your name: ").strip().title()
                        try:
                            p = int(input("Enter PIN: "))
                            self.login(n, p)
                        except ValueError:
                            print("Error: PIN must be a number.")

                    case "3":
                        print("System shutting down...")
                        break
                    case _:
                        print("Invalid Option")

            else:
                print(f"\n--- Menu for {self.current_user.name} ---")
                acc_type = type(self.current_user).__name__
                print(f"Type: {acc_type}")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. View History")
                print("5. Logout")
                Action = input("What would you like to do? ")

                match Action:
                    case "1":
                        print(f"Current Balance: {self.current_user.check_balance():,}")
                    case "2":
                        try:
                            amount = int(input("Amount to deposit: "))
                            self.current_user.deposit(amount)
                            self.save_data()
                        except ValueError:
                            print("Error: Please enter a valid number.")
                    case "3":
                        try:
                            amount = int(input("Amount to withdraw: "))
                            self.current_user.withdraw(amount)
                            self.save_data()
                        except ValueError:
                            print("Error: Please enter a valid number.")
                    case "4":
                        print("\n--- Transaction History ---")
                        history = self.current_user.get_history()
                        if not history:
                            print("No transactions yet.")
                        else:
                            for record in history:
                                print(record)
                        input("\nPress Enter to continue...")
                    case "5":
                        self.logout()
                    case _:
                        print("Invalid Option")