"""
QUESTION:
Create a function `below_zero` that takes a list of integers representing deposit and withdrawal operations on a bank account with an initial balance of zero. The function should return a tuple containing a boolean indicating whether the balance falls below zero at any point and the final balance. The function should stop updating the balance as soon as it falls below zero.
"""

def below_zero(operations: list[int]) -> tuple[bool, int]:
    balance = 0
    below_zero_flag = False
    for op in operations:
        balance += op
        if balance < 0:
            below_zero_flag = True
            break
            
    return below_zero_flag, balance