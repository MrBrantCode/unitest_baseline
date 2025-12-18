"""
QUESTION:
Write a function `display_transactions(account_name, accounts)` that takes the account name and a list of accounts as input, prints all the transactions for the specified account, and returns the total balance. If the account does not exist, it should print "Account not found" and return 0.
"""

class Transaction:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class Account:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

    def display_transactions(self):
        if self.transactions:
            print(f"Transactions for {self.name}:")
            for transaction in self.transactions:
                print(f"{transaction.date} - {transaction.description}: {transaction.amount}")
        else:
            print("No transactions found for this account")

def display_transactions(account_name, accounts):
    found = False
    for account in accounts:
        if account.name == account_name:
            account.display_transactions()
            print(f"Balance for {account_name}: {account.calculate_balance()}")
            found = True
            return account.calculate_balance()
    if not found:
        print("Account not found")
        return 0