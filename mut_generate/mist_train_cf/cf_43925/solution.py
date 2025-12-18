"""
QUESTION:
Implement a function called `below_zero` that takes a dictionary `operations` and an optional boolean parameter `case_insensitive` (defaulting to `False`) as input. The dictionary has account numbers as keys and lists of tuples containing operation type and value as values. The function should track the balance of each account, raise an `InsufficientBalanceException` if the balance goes below zero, and return a dictionary of account numbers that maintained a positive balance throughout the operations. If `case_insensitive` is `True`, the function should treat 'Deposit' and 'deposit', 'Withdrawal' and 'withdrawal' as identical and consider a balance of zero as positive.
"""

from typing import List, Tuple, Dict

class InsufficientBalanceException(Exception):
    pass

def below_zero(operations: Dict[int, List[Tuple[str, int]]], case_insensitive: bool = False) -> Dict[int, str]:
    positive_balance_accounts = {}
    
    for account, ops in operations.items():
        balance = 0
        for op in ops:
            operation, amount = op
            if case_insensitive:
                operation = operation.lower()
            if operation in ['deposit', 'd']:
                balance += amount
            elif operation in ['withdrawal', 'w']:
                if balance - amount < 0:
                    raise InsufficientBalanceException(f'Account {account} has insufficient balance.')
                balance -= amount
        positive_balance_accounts[account] = 'No negative balance'
    
    return positive_balance_accounts