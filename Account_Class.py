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
            "type": "Standard",
            "name": self.name.title(),
            "pin": self.pin,
            "balance": self.balance
        }
    
class Saving_Accounts(Account):
    def __init__(self, name, pin, balance,interest_rate = 0.05):
        super().__init__(name, pin, balance)
        self.interest_rate = interest_rate

    def deposit(self,amount):
        if amount > 0:
            Interest = amount * self.interest_rate
            Total = amount + Interest
            self.balance += Total
            print(f"Deposited: ${amount} + ${Interest} (Interest). New Balance: ${self.balance}")
        else:
            print("Error: Deposit amount must be positive.")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Savings"
        return data