"""
QUESTION:
Write a function `calculate_fibonacci` to calculate the nth number of the Fibonacci sequence using iteration. The function should accept a list of starting values for the Fibonacci sequence. It should have three parameters: `n`, `a`, and `b`, where `n` is the position in the sequence, and `a` and `b` are the first two numbers in the sequence with default values of 0 and 1, respectively.
"""

def calculate_fibonacci(n, a=0, b=1):
    """
    This function calculates the nth number of the Fibonacci sequence using iteration,
    starting from the given values a and b.
    
    Parameters:
        n (int): The number in the Fibonacci sequence to calculate.
        a (int): The first value in the Fibonacci sequence (default: 0).
        b (int): The second value in the Fibonacci sequence (default: 1).
        
    Returns:
        The nth number of the Fibonacci sequence.
    """
    if n <= 1:
        return a if n == 0 else b
    
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
        
    return b