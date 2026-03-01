class BankAccount:

    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        
    def showbalance(self):
        self.balance = self.balance
    