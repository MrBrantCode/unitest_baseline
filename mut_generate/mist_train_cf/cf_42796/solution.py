"""
QUESTION:
Create a Python function named `banking_operations` that simulates a simple banking system. The function should take in three parameters: `account_balance`, `amount_to_deposit`, and `amount_to_withdraw`, which are all integers representing the current account balance, the amount to deposit, and the amount to withdraw respectively. The function should perform the deposit and withdrawal operations and return the updated account balance. The function should not allow the account balance to go below zero.
"""

def banking_operations(account_balance, amount_to_deposit, amount_to_withdraw):
    updated_balance = account_balance + amount_to_deposit - amount_to_withdraw
    if updated_balance < 0:
        return "Insufficient funds"
    else:
        return updated_balance