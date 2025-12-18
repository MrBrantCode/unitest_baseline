"""
QUESTION:
Design a function named `fibonacci_numbers` that generates Fibonacci numbers up to a given maximum value `max_value`. The function should have a time complexity of O(n) and space complexity of O(1), where n is the maximum value. The function should handle large maximum values (up to 10^18) efficiently and accurately.
"""

def fibonacci_numbers(max_value):
    """
    Generates Fibonacci numbers up to a given maximum value.
    
    Args:
    max_value (int): The maximum value up to which Fibonacci numbers are generated.
    
    Returns:
    list: A list of Fibonacci numbers up to the given maximum value.
    """
    fib_numbers = []
    a, b = 0, 1
    while a <= max_value:
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers