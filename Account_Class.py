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