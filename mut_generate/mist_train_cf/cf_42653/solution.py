"""
QUESTION:
Create a function `analyzer` that takes an integer `n` as input. The function should return a string that includes the input value, its predecessor (`n-1`), and its successor (`n+1`) in the following format: 'Analisando o valor {n}, seu antecessor é {predecessor} e o sucessor é {successor}'.
"""

def analyzer(n):
    """
    Analyzes the input value and returns a string containing the input value, 
    its predecessor (n-1), and its successor (n+1).

    Args:
        n (int): The input value to be analyzed.

    Returns:
        str: A formatted string containing the input value, its predecessor, and its successor.
    """
    predecessor = n - 1
    successor = n + 1
    return f'Analisando o valor {n}, seu antecessor é {predecessor} e o sucessor é {successor}'