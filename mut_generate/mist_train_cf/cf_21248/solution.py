"""
QUESTION:
Write a function named `fibonacci_calculations` that generates a Fibonacci sequence up to a given number `n` and returns the sum of the even numbers in the sequence and the product of the odd numbers in the sequence. The sequence should include the first two numbers of the Fibonacci sequence, 0 and 1. The function should only consider numbers in the sequence that are less than or equal to `n`.
"""

def fibonacci_calculations(n):
    """
    Generates a Fibonacci sequence up to a given number n and returns the sum of the even numbers in the sequence and the product of the odd numbers in the sequence.
    
    Args:
        n (int): The upper limit of the Fibonacci sequence.
    
    Returns:
        tuple: A tuple containing the sum of the even numbers in the sequence and the product of the odd numbers in the sequence.
    """
    a, b = 0, 1
    even_sum, odd_product = 0, 1
    
    while a <= n:
        if a % 2 == 0:
            even_sum += a
        else:
            odd_product *= a
        
        a, b = b, a + b
    
    return even_sum, odd_product