"""
QUESTION:
Construct a function named `square_cumulative_fibonacci(n)` that takes an integer `n` as input and returns the cumulative total of the squared values derived from the Fibonacci sequence, considering up to `n` elements in the series. The function should handle edge cases where `n` is less than or equal to 0, and return an appropriate error message or value.
"""

def square_cumulative_fibonacci(n):
    """
    Calculate the cumulative total of the squared values derived from the Fibonacci sequence, 
    considering up to n elements in the series.

    Args:
    n (int): The number of elements in the Fibonacci sequence.

    Returns:
    int or str: The cumulative sum of the squares of the Fibonacci numbers if n > 0, 
    otherwise an error message.
    """
    
    # Initialize the first two fibonacci numbers
    fibonacci_sequence = [0, 1]
    squared_cumulative_sum = 0
    
    # Check if n is less than 2 and return the required outputs
    if n <= 0:
        return "n should be greater than 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Generate the fibonacci sequence up to n
        for i in range(2, n):
            fibonacci_next = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
            fibonacci_sequence.append(fibonacci_next)
        
        # Compute the cumulative sum of squares of the fibonacci numbers
        for i in range(n):
            squared_cumulative_sum += fibonacci_sequence[i] ** 2
            
    return squared_cumulative_sum