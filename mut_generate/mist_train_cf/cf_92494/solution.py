"""
QUESTION:
Design a BankAccount class with a constructor that takes name, balance, and interest_rate as parameters and has methods to deposit, withdraw, and calculate interest. Ensure the balance is restricted to positive values and the interest_rate is between 0 and 10. The deposit and withdraw methods should update the balance correctly and prevent it from going below zero.
"""

def bank_account(name, balance, interest_rate):
    balance = max(0, balance)  # Restrict balance to positive values
    interest_rate = max(0, min(interest_rate, 10))  # Restrict interest_rate to a range between 0 and 10
    
    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
    
    def withdraw(amount):
        nonlocal balance
        if amount > 0 and amount <= balance:
            balance -= amount
    
    def calculate_interest():
        return balance * (interest_rate / 100)
    
    return deposit, withdraw, calculate_interest