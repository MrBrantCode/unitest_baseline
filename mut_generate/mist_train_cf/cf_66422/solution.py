"""
QUESTION:
Write two functions, `product_odd(n)` and `product_even(n)`, that take a positive integer `n` as input and return the product of all odd and even numbers up to and including `n`, respectively. The functions should have a time complexity in Big O notation.
"""

def product_odd(n):
    """
    Calculate the product of all odd numbers up to and including n.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        int: The product of all odd numbers up to and including n.
    """
    product = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            product *= i
    return product

def product_even(n):
    """
    Calculate the product of all even numbers up to and including n.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        int: The product of all even numbers up to and including n.
    """
    product = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            product *= i
    return product