"""
QUESTION:
Create a function called `get_fibonacci_sequence` that takes an integer `n` as an argument. The function should return a list containing the Fibonacci sequence up to `n` numbers. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, usually starting with 0 and 1. The function should be able to handle cases where `n` is less than or equal to 2.
"""

def get_fibonacci_sequence(n):
    """Returns a list containing the Fibonacci sequence up to number n"""
    fib_list = [0, 1]
    if n <= 2:
        return fib_list[:n]
    
    for i in range(2, n):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    
    return fib_list