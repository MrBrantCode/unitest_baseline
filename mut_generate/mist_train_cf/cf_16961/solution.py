"""
QUESTION:
Write a function `fibonacci_sequence(n)` that uses a while loop to generate and return the Fibonacci sequence up to the nth term, as well as the sum of all the Fibonacci numbers in the sequence. The function should take an integer `n` as input, where 2 < n < 100.
"""

def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to the nth term and return the sequence along with the sum of all the Fibonacci numbers.
    
    Args:
        n (int): The number of terms in the Fibonacci sequence. Should be greater than 2 and less than 100.
    
    Returns:
        tuple: A tuple containing the Fibonacci sequence and the sum of all the Fibonacci numbers.
    """
    
    # Initialize variables
    fib_sequence = [0, 1]
    sum_of_fib = 1

    # Generate Fibonacci sequence
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        sum_of_fib += next_fib

    return fib_sequence, sum_of_fib