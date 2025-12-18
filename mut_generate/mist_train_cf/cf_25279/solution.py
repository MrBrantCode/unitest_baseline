"""
QUESTION:
Create a function called `gen_list` that generates a list of length `n` containing all numbers from 1 to `n`. The function should take an integer `n` as input and return a list of integers.
"""

def gen_list(n):
    """Generates a list of length `n` containing all numbers from 1 to `n`.
    
    Args:
        n (int): The length of the list to be generated.
    
    Returns:
        list: A list of integers from 1 to `n`.
    """
    list = []
    for i in range(1, n+1):
        list.append(i)
    return list