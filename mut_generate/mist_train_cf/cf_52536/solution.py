"""
QUESTION:
The function `account_transactions` takes a list of tuples, where each tuple represents a bank transaction in the format `(account_number, operation_type, operation_value)`. It should return `True` if the balance of any account falls below zero at any point, and `False` otherwise. The function should also return an error message 'Invalid operation encountered.' if an account number is incorrect, if a credit amount is below zero, or if a debit operation exceeds the present balance.
"""

from typing import List, Tuple, Union

def account_transactions(accounts_transactions: List[Tuple[int, str, int]]) -> Union[bool, str]:
   
    balances = {}
    
    for account_number, operation_type, operation_value in accounts_transactions:
        if operation_value < 0: 
            return 'Invalid operation encountered.'
        
        if operation_type == 'Deposit':
            if account_number in balances:
                balances[account_number] += operation_value
            else:
                balances[account_number] = operation_value
                
        elif operation_type == 'Withdrawal':
            if account_number in balances:
                if operation_value > balances[account_number]:
                    return 'Invalid operation encountered.'
                else:
                    balances[account_number] -= operation_value
                if balances[account_number] < 0:
                    return True
            else:
                return 'Invalid operation encountered.'
        else:
            return 'Invalid operation encountered.'
    
    if any(balance < 0 for balance in balances.values()):
        return True
    else:
        return False