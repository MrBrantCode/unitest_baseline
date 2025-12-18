"""
QUESTION:
Create a `BankAccount` class with an `account_number` attribute and a `balance` attribute initialized to 0. The class should have methods to deposit, withdraw, and get the balance. Also, implement a function `create_account(account_number)` that creates and returns a new `BankAccount` object with the given account number.

The `BankAccount` class should have the following methods:
- `__init__(self, account_number)`: initializes the account with the given account number.
- `deposit(self, amount)`: adds the given amount to the account balance.
- `withdraw(self, amount)`: subtracts the given amount from the account balance if sufficient funds are available.
- `get_balance(self)`: returns the current balance of the account.
"""

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


def create_account(account_number):
    return BankAccount(account_number)