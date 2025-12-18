"""
QUESTION:
Create a class named "Account" that represents a bank account with a unique account number, a holder name, and a current balance. The class should have methods to withdraw, deposit, and get the current balance. The withdraw method should raise a custom exception called "InsufficientFundsException" if the withdrawal amount is greater than the current balance. Implement a logging mechanism to log any exceptions raised during the program execution.
"""

import logging
import datetime

# Custom exception for insufficient funds
class InsufficientFundsException(Exception):
    pass

def account(account_number, holder_name, balance=0):
    """
    Represents a bank account with a unique account number, a holder name, and a current balance.
    
    Methods:
    withdraw(amount): Withdraws the specified amount from the account.
    deposit(amount): Deposits the specified amount into the account.
    get_balance(): Returns the current balance of the account.
    """
    class Account:
        def __init__(self, account_number, holder_name, balance=0):
            self.account_number = account_number
            self.holder_name = holder_name
            self.balance = balance
        
        def withdraw(self, amount):
            if amount > self.balance:
                raise InsufficientFundsException("Insufficient funds to withdraw.")
            self.balance -= amount
        
        def deposit(self, amount):
            self.balance += amount
        
        def get_balance(self):
            return self.balance
    
    return Account(account_number, holder_name, balance)