"""
QUESTION:
Write a function `collatz(n)` that generates the Collatz sequence starting from a positive integer `n` up to 1. The function should calculate and return the total number of steps to reach 1 and the highest number encountered in the sequence. The sequence is defined as: if `n` is even, the next term is `n/2`; if `n` is odd, the next term is `3n+1`. Optimize the function for large values of `n`, up to 10^6.
"""

def collatz(n):
    """
    Generates the Collatz sequence starting from a positive integer n up to 1.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        tuple: A tuple containing the total number of steps to reach 1 and the highest number encountered in the sequence.
    """
    steps = 0
    highest_number = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # Using integer division to avoid float results
        else:
            n = 3 * n + 1
        if n > highest_number:
            highest_number = n
        steps += 1
    return steps, highest_number