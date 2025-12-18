"""
QUESTION:
Create a function `fibonacci_sequence(n)` that generates the first `n` numbers of the Fibonacci sequence, where `n` is a positive integer. The function should return a list of the first `n` Fibonacci numbers.
"""

def fibonacci_sequence(n):
    """
    Generates the first n numbers of the Fibonacci sequence.
    
    Args:
        n (int): A positive integer representing the number of Fibonacci numbers to generate.
    
    Returns:
        list: A list of the first n Fibonacci numbers.
    """
    fibonacci_list = [0, 1]
    for i in range(2, n):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    return fibonacci_list[:n]