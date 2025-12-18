"""
QUESTION:
Create a function called `fibonacci_sequence()` that generates a Fibonacci sequence based on user input. The input should be a positive integer greater than 1. The function should handle invalid inputs by prompting the user for a valid input and display informative error messages when necessary. The generated Fibonacci sequence should be printed in reverse order.
"""

def fibonacci_sequence(n):
    """
    Generates a Fibonacci sequence based on user input and prints it in reverse order.
    
    Args:
    n (int): The number of terms in the Fibonacci sequence.
    
    Returns:
    list: The generated Fibonacci sequence in reverse order.
    """
    sequence = []
    a, b = 0, 1
    
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence[::-1]