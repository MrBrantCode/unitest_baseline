"""
QUESTION:
Create a function `balanceControlAndRollBack` that takes two parameters: `operations` (a list of integers) and `rollBackSteps` (an integer). Implement a transaction rollback framework to prevent the account balance from going below zero. The function should roll back the last 'n' transactions if the balance becomes negative and return the final balance, which should never be less than zero.
"""

from collections import deque

def balanceControlAndRollBack(operations: list, rollBackSteps: int):
    balance = 0
    past_operations = deque(maxlen=rollBackSteps)
    
    for op in operations:
        balance += op
        past_operations.append(op)
        
        if balance < 0:
            while balance < 0 and past_operations:
                rollBackOp = past_operations.pop()
                balance -= rollBackOp
    return max(0, balance)