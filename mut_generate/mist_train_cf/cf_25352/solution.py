"""
QUESTION:
Write a function `get_fibonacci(n)` that generates the first n terms of the Fibonacci sequence. The function should take an integer `n` as input and return a list of the first n Fibonacci numbers. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def generate_fibonacci(n):
    """ Generates n terms of the Fibonacci sequence
    
    Args:
        n (int): The number of Fibonacci terms to generate
        
    Returns:
        list: A list of the first n Fibonacci numbers
    """
    # Initialize first two Fibonacci numbers
    a = 0
    b = 1

    # Initialize the Fibonacci Sequence list
    fibonacci_sequence = []
    fibonacci_sequence.append(a)
    fibonacci_sequence.append(b)

    # Generate the Fibonacci Sequence
    while len(fibonacci_sequence) < n:
        c = a + b
        fibonacci_sequence.append(c)
        a = b
        b = c

    return fibonacci_sequence