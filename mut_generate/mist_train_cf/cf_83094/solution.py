"""
QUESTION:
Write a function named `print_even` that takes an integer `n` as input and recursively prints the even numbers from `n` to 0 in descending order. The function should include input validation to handle cases where `n` is a negative integer.
"""

def print_even(n):
    """
    Recursively prints the even numbers from n to 0 in descending order.
    
    Args:
    n (int): A non-negative integer.
    """
    if n < 0: 
        print("Error: Input must be non-negative integer")  
        return
    elif n % 2 != 0:  
        print_even(n-1)
    else: 
        print(n)
        if n > 0:
            print_even(n-2)