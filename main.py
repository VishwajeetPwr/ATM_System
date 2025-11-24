import json
import os

try: 
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    SCRIPT_DIR = os.getcwd()

DB_PATH = os.path.join(SCRIPT_DIR, "ATM_Database.json")

class Account:
    def __init__(self, name, pin, balance):
        self.name = name.title()
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Amount: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Amount: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")    
    
    def to_dict(self):
        return {
            "name": self.name.title(),
            "pin": self.pin,
            "balance": self.balance
        }

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
                
            # Convert Dict -> Object
                for name, info in data.items():
                    # Re-creating the object from the saved data
                    recreated_acc = Account(info['name'], info['pin'], info['balance'])
                    self.accounts[name] = recreated_acc
        except (FileNotFoundError, json.JSONDecodeError):
            # File doesn't exist on first run. That's okay.
            self.accounts = {}

    def create_account(self, name, pin, balance):
        if name in self.accounts:
            print("Account already exists.")
            return
        
        new_account = Account(name, pin, balance)
        self.accounts[name] = new_account
        self.save_data()
        print(f"Account created for {name} with balance {balance}")
    
    def login(self, name, pin):
        if name in self.accounts:
            if self.accounts[name].pin == pin:
                self.current_user = self.accounts[name]
                print(f"Login successful. Welcome, {name}!")
                return True
            else:
                print("Error: Incorrect PIN.")
        else:
            print("Incorrect PIN.")

    def logout(self):
        if self.current_user:
            print(f"Goodbye, {self.current_user.name}!")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    

    def run(self):
        print("===ATM System Started===")

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
                            self.create_account(n, p, b)
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
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")
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
                    case"3":
                        try:
                            amount = int(input("Amount to withdraw: "))
                            self.current_user.withdraw(amount)
                            self.save_data()
                        except ValueError:
                            print("Error: Please enter a valid number.")
                    case "4":
                        self.logout()
                    case _:
                        print("Invalid Option")


if __name__ == "__main__":
    app = ATM()
    app.run()

