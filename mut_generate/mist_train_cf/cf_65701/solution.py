"""
QUESTION:
Implement the `below_zero` function, which takes a list of deposit and withdrawal operations on a bank account and an optional case_insensitive flag. The function should return True if the balance falls below zero at any point, False otherwise. If the case_insensitive flag is True, treat 'Deposit' and 'deposit', as well as 'Withdrawal' and 'withdrawal', as the same and return True if the balance equals zero. If an invalid operation is encountered, return an error message stating, "Invalid operation encountered." The input list contains tuples in the format (Operation_type, Operation_value). The function should handle all possible edge cases.
"""

from typing import List, Tuple, Union

def below_zero(operations: List[Tuple[str, int]], case_insensitive: bool = False) -> Union[bool, str]:
    balance = 0
    for op_type, op_val in operations:
        if case_insensitive:
            op_type = op_type.lower()
        
        if op_type == 'deposit':
            balance += op_val
        elif op_type == 'withdrawal':
            balance -= op_val
            if balance < 0:
                return True
        else:
            return 'Invalid operation encountered.'
    
    if case_insensitive and balance == 0:
        return True
    return False