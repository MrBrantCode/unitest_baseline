"""
QUESTION:
Create a `BankAccount` class with an `__init__` method that takes the account holder's name and an initial balance (defaulted to 0). Implement `deposit`, `withdraw`, and `get_balance` methods. The `deposit` method should update the account balance by adding the deposited amount. The `withdraw` method should update the account balance by subtracting the withdrawn amount if sufficient funds are available, otherwise print "Insufficient funds" and leave the balance unchanged. The `get_balance` method should return the current balance of the account.
"""

def bank_account(account_holder, initial_balance=0):
    class BankAccount:
        def __init__(self, account_holder, initial_balance):
            self.account_holder = account_holder
            self.balance = initial_balance

        def deposit(self, amount):
            self.balance += amount

        def withdraw(self, amount):
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds")

        def get_balance(self):
            return self.balance
    return BankAccount(account_holder, initial_balance)