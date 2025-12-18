"""
QUESTION:
Write a function that demonstrates the concept of recursion and explains how it works. The function should describe the process of recursion, including the execution of recurring steps and the termination condition.
"""

def recursion_example(n):
    """
    A recursive function that demonstrates the concept of recursion.
    
    Args:
        n (int): The number of recurrence steps.
    
    Returns:
        str: A string describing the process of recursion.
    """
    if n == 0:
        return "Termination condition reached."
    else:
        return f"Recurrence step {n}. " + recursion_example(n-1)