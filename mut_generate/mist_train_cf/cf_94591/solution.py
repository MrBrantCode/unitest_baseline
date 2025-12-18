"""
QUESTION:
Create a Python function `calculate_interest(balance)` and a class `BankAccount(account_number, balance)` to simulate a simple bank account system. The `calculate_interest` function should calculate the interest rate for a given balance based on a fixed interest rate of 5%. The `BankAccount` class should have methods to deposit and withdraw money, and include error handling to handle potential exceptions, such as invalid deposit or withdrawal amounts and insufficient balance. The code should also demonstrate the usage of both functions and classes together.
"""

# Function to calculate the interest rate for a given balance
def calculate_interest(balance):
    try:
        interest_rate = 0.05  # Assuming a fixed interest rate of 5%
        interest = balance * interest_rate
        return interest
    except TypeError:
        print("Invalid balance type.")
        return 0

# Class representing a bank account
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        try:
            self.balance += amount
        except TypeError:
            print("Invalid deposit amount.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance.")
        except TypeError:
            print("Invalid withdrawal amount.")