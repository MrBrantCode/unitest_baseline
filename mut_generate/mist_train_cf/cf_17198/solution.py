"""
QUESTION:
Implement a function `calculate_interest` that takes a balance as input and returns the calculated interest based on a fixed interest rate, and a `BankAccount` class that represents a bank account with methods to deposit and withdraw money. The function and class should include error handling to handle potential exceptions. The `BankAccount` class should have an attribute to store the account number. The interest rate should be assumed as 5%.
"""

def calculate_interest(balance):
    """
    Calculate the interest based on a fixed interest rate of 5%.
    
    Args:
    balance (float): The current balance in the account.
    
    Returns:
    float: The calculated interest.
    """
    try:
        interest_rate = 0.05  
        interest = balance * interest_rate
        return interest
    except TypeError:
        print("Invalid balance type.")
        return 0


class BankAccount:
    def __init__(self, account_number, balance):
        """
        Initialize the BankAccount object.
        
        Args:
        account_number (str): The unique account number.
        balance (float): The initial balance in the account.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
        amount (float): The amount to be deposited.
        """
        try:
            self.balance += amount
        except TypeError:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
        amount (float): The amount to be withdrawn.
        """
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance.")
        except TypeError:
            print("Invalid withdrawal amount.")