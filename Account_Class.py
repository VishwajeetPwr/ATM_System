import datetime
class Account:
    def __init__(self, name, pin, balance,history = None):
        self.name = name.title()
        self.pin = pin
        self.balance = balance
        self.history = history if history else []

    def check_balance(self):
        return self.balance
    
    def add_transaction(self,message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = f"[{timestamp}] {message}"
        self.history.append(record)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.add_transaction(f"Deposited: ${amount}")
            print(f"Deposited Amount: {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.add_transaction(f"Withdrew: ${amount}")
            print(f"Withdrew Amount: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")    
    
    def get_history(self):
        return self.history
    
    def to_dict(self):
        return {
            "type": "Standard",
            "name": self.name.title(),
            "pin": self.pin,
            "balance": self.balance,
            "history": self.history
        }
    
class Saving_Accounts(Account):
    def __init__(self, name, pin, balance,interest_rate = 0.05,history = None):
        super().__init__(name, pin, balance,history)
        self.interest_rate = interest_rate

    def deposit(self,amount):
        if amount > 0:
            Interest = amount * self.interest_rate
            Total = amount + Interest
            self.balance += Total
            self.add_transaction(f"Deposited: ${amount} + ${Interest} (Interest)")
            print(f"Deposited: ${amount} + ${Interest} (Interest). New Balance: ${self.balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Savings"
        return data