"""
QUESTION:
Write a function named even_number_sequence that generates a string of all even numbers from 0 to n, separated by commas. The function should take an integer n as input and return a string. The function should be able to handle cases where n is 0 or any other non-negative integer.
"""

def even_number_sequence(n):
    """Generates a string of all even numbers from 0 to n, separated by commas."""
    return ",".join(str(i) for i in range(0, n + 1, 2))