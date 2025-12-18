"""
QUESTION:
Implement the function `fibonacci_sum(n)`, where:
- n: An integer representing the nth number in the Fibonacci sequence (1 <= n <= 10^6).

The function should return the sum of the Fibonacci sequence up to the nth number, with a time complexity of O(n), without using recursion, and handle large values of n efficiently without causing any overflow errors.
"""

def fibonacci_sum(n):
    """
    Calculate the sum of the Fibonacci sequence up to the nth number.

    Args:
    n (int): An integer representing the nth number in the Fibonacci sequence (1 <= n <= 10^6).

    Returns:
    int: The sum of the Fibonacci sequence up to the nth number.
    """
    if n <= 1:
        return n
    
    # Initialize a list to store Fibonacci numbers and their sum
    fib_sequence = [0, 1]
    fib_sum = 1
    
    # Calculate Fibonacci numbers and their sum
    for i in range(2, n + 1):
        next_fib = fib_sequence[0] + fib_sequence[1]
        fib_sequence[0] = fib_sequence[1]
        fib_sequence[1] = next_fib
        fib_sum += next_fib
    
    return fib_sum