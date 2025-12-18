"""
QUESTION:
Implement the following functions in a Python module: `create_account`, `deposit`, `withdraw`, and `generate_statement`. 

The `create_account` function should take an account number and initial balance as parameters and return a new `BankAccount` object. The `BankAccount` class should have `account_number`, `balance`, and `transactions` attributes.

The `deposit` and `withdraw` functions should take a `BankAccount` object, amount, date, and description as parameters and update the account balance and transactions accordingly. The `withdraw` function should prevent overdrafts.

The `generate_statement` function should take a `BankAccount` object as a parameter and return a statement including the account number, current balance, and a list of transactions with their details.

The module should also include a `Transaction` class with `date`, `amount`, and `description` attributes.
"""

class Transaction:
    def __init__(self, date, amount, description):
        self.date = date
        self.amount = amount
        self.description = description

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

def create_account(account_number, initial_balance):
    return BankAccount(account_number, initial_balance)

def deposit(account, amount, date, description):
    account.balance += amount
    transaction = Transaction(date, amount, description)
    account.transactions.append(transaction)

def withdraw(account, amount, date, description):
    if amount <= account.balance:
        account.balance -= amount
        transaction = Transaction(date, -amount, description)
        account.transactions.append(transaction)
    else:
        print("Insufficient funds")

def generate_statement(account):
    statement = f"Account Number: {account.account_number}\nCurrent Balance: {account.balance}\nTransactions:\n"
    for transaction in account.transactions:
        statement += f"{transaction.date} - {transaction.amount} - {transaction.description}\n"
    return statement