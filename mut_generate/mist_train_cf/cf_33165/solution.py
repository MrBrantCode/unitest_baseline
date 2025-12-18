"""
QUESTION:
Implement a Python class named `BankAccount` with methods `__init__(self, account_number, initial_balance)`, `deposit(self, amount)`, `withdraw(self, amount)`, and `get_balance(self)`. The class should handle exceptions for `InvalidTransactionException` and `InvalidAmountException`. The `__init__` method should initialize the account with the given account number and initial balance. The `deposit` and `withdraw` methods should add to and subtract from the account balance respectively, but raise `InvalidAmountException` for negative amounts and `InvalidTransactionException` for withdrawing more than the available balance. The `get_balance` method should return the current account balance.
"""

class InvalidTransactionException(Exception):
    pass

class InvalidAmountException(Exception):
    pass

def BankAccount(account_number, initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if amount < 0:
            raise InvalidAmountException("Invalid amount for deposit")
        balance += amount

    def withdraw(amount):
        nonlocal balance
        if amount < 0:
            raise InvalidAmountException("Invalid amount for withdrawal")
        if amount > balance:
            raise InvalidTransactionException("Insufficient funds for withdrawal")
        balance -= amount

    def get_balance():
        return balance

    return deposit, withdraw, get_balance