"""
QUESTION:
Implement the `BankAccount` class with the following specifications:
- The class should have a constructor that takes the account holder's name and initializes the balance to 0.
- The class should have methods for depositing funds, withdrawing funds, checking the balance, and transferring funds to another account.
- The `deposit` method should take an amount as a parameter and add it to the balance.
- The `withdraw` method should take an amount as a parameter and subtract it from the balance if the balance is sufficient; otherwise, it should print "Insufficient funds".
- The `get_balance` method should return the current balance.
- The `transfer` method should take another `BankAccount` object and an amount as parameters and transfer the specified amount from the current account to the other account if the balance is sufficient; otherwise, it should print "Insufficient funds".
"""

def BankAccount(account_holder):
    balance = 0

    def deposit(amount):
        nonlocal balance
        balance += amount

    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance -= amount
        else:
            print("Insufficient funds")

    def get_balance():
        return balance

    def transfer(other_account, amount):
        nonlocal balance
        if balance >= amount:
            balance -= amount
            other_account.deposit(amount)
        else:
            print("Insufficient funds")

    return locals()