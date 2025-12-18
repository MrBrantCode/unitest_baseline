"""
QUESTION:
Write a function named `generate_fibonacci_series` to generate a Fibonacci series of n terms, where n is a positive integer greater than or equal to 2. The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return the generated Fibonacci series as a list of integers.
"""

def generate_fibonacci_series(n):
    """
    Generate a Fibonacci series of n terms.

    Args:
    n (int): The number of terms in the Fibonacci series.

    Returns:
    list: A list of integers representing the Fibonacci series.

    """
    # Initialize the first two terms of the series
    first_term = 0
    second_term = 1
    
    # Initialize the Fibonacci series with the first two terms
    fibonacci_series = [first_term, second_term]
    
    # Generate the Fibonacci series till n terms
    while len(fibonacci_series) < n:
        # Calculate the next term by adding the previous two terms
        next_term = first_term + second_term
        
        # Append the next term to the Fibonacci series
        fibonacci_series.append(next_term)
        
        # Update the values of first_term and second_term
        first_term = second_term
        second_term = next_term
    
    return fibonacci_series