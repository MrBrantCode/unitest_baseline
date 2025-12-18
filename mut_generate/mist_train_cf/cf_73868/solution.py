"""
QUESTION:
Create a function named `below_zero` that takes two parameters: `operations` and `case_insensitive`. `operations` is a list of tuples containing the operation type and value, and `case_insensitive` is a boolean flag that defaults to `False`. The function should calculate the lowest balance point reached throughout the operations. If `case_insensitive` is `True`, the function should treat 'Deposit' and 'deposit', 'Withdrawal' and 'withdrawal' as equals. The function should return the lowest balance point.
"""

def below_zero(operations, case_insensitive=False):
    balance = 0
    low = 0

    for operation in operations:
        op, value = operation
        if case_insensitive:
            op = op.lower()
        if op == 'deposit':
            balance += value
        elif op == 'withdrawal':
            balance -= value
        if balance < low: 
            low = balance
    return low