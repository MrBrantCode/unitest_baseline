"""
QUESTION:
Implement a function called `account_transcations` that accepts a list of bank transactions, each represented as a tuple of (account_number, operation_type, operation_value), and returns True if the balance of any account falls below zero at any point, False otherwise. If an account number is invalid or if a deposit amount is negative or if a withdrawal operation exceeds the current balance, return an error message stating "Invalid operation encountered."
"""

from typing import List, Tuple, Union

def account_transcations(accounts_transactions: List[Tuple[int, str, int]]) -> Union[bool, str]:
    accounts = {}
    
    for account, operation, amount in accounts_transactions:
        # create account if it does not exist
        if account not in accounts:
            accounts[account] = 0

        # check for deposit operations
        if operation.lower() == 'deposit':
            if amount < 0:
                return "Invalid operation encountered."
            accounts[account] += amount
        # check for withdrawal operations
        elif operation.lower() == 'withdrawal':
            if amount > accounts[account]:
                return "Invalid operation encountered."
            accounts[account] -= amount
        
        # check if the balance has gone below 0
        if accounts[account] < 0:
            return True

    # if we reached here, it means there has been no case of negative balance
    return False