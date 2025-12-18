"""
QUESTION:
Create a Python class `BankAccount` with the following specifications:

- The class should be initialized with the account holder's name and an initial balance.
- The class should have methods `deposit`, `withdraw`, `get_balance`, and `get_total_transactions`.
- The `deposit` method should take an amount as a parameter, add it to the account balance, and increment the total number of transactions.
- The `withdraw` method should take an amount as a parameter, subtract it from the account balance if the withdrawal amount is less than or equal to the current balance, and increment the total number of transactions.
- The `get_balance` method should return the current account balance.
- The `get_total_transactions` method should return the total number of transactions made on the account.
"""

def BankAccount(account_holder, initial_balance):
    balance = initial_balance
    total_transactions = 0

    def deposit(amount):
        nonlocal balance, total_transactions
        balance += amount
        total_transactions += 1

    def withdraw(amount):
        nonlocal balance, total_transactions
        if amount <= balance:
            balance -= amount
            total_transactions += 1
        else:
            print("Insufficient funds")

    def get_balance():
        return balance

    def get_total_transactions():
        return total_transactions

    return deposit, withdraw, get_balance, get_total_transactions