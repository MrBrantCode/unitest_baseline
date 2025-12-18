"""
QUESTION:
Implement a function `find_nth_fibonacci_number_in_range(start: int, end: int, n: int) -> int` that returns the nth Fibonacci number in the range [start, end]. The Fibonacci sequence is defined as the sequence of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return -1 if the nth Fibonacci number is not in the range.
"""

def find_nth_fibonacci_number_in_range(start: int, end: int, n: int) -> int:
    """
    Returns the nth Fibonacci number in the range [start, end].
    
    Args:
    start (int): The start of the range.
    end (int): The end of the range.
    n (int): The position of the Fibonacci number to find.
    
    Returns:
    int: The nth Fibonacci number in the range [start, end], or -1 if it's not found.
    """
    
    # Initialize an empty list to store the Fibonacci numbers
    fibonacci_sequence = []
    
    # Initialize num1 and num2 as the first two Fibonacci numbers
    num1, num2 = 0, 1
    
    # Loop through the Fibonacci sequence until the current Fibonacci number is greater than or equal to the end value
    while num2 <= end:
        # If the current Fibonacci number is greater than or equal to the start value, append it to the fibonacci_sequence list
        if num2 >= start:
            fibonacci_sequence.append(num2)
        
        # Calculate the next Fibonacci number by adding num1 and num2
        num1, num2 = num2, num1 + num2
    
    # If n is within the range of the Fibonacci sequence, return the nth Fibonacci number. Otherwise, return -1
    return fibonacci_sequence[n - 1] if n <= len(fibonacci_sequence) else -1