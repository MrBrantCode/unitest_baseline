"""
QUESTION:
Implement a `BankAccount` class with private attributes for balance and overdraft limit. The class should have a constructor that initializes these attributes, a `deposit` method that adds funds to the account, a `withdraw` method that deducts funds and allows overdrafts up to a certain limit, and a `get_balance` method that returns the current balance. Ensure that the balance and overdraft limit are not directly accessible from outside the class.
"""

def bank_account(initial_balance, overdraft_limit):
    balance = initial_balance
    def deposit(amount):
        nonlocal balance
        balance += amount
    def withdraw(amount):
        nonlocal balance
        if balance - amount >= -overdraft_limit:
            balance -= amount
        else:
            print("Withdrawal amount exceeds overdraft limit")
    def get_balance():
        return balance
    return deposit, withdraw, get_balance