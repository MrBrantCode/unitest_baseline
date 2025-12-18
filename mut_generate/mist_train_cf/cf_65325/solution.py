"""
QUESTION:
Implement a function to compute the nth Fibonacci number using recursive and iterative approaches, and optimize the recursive solution with memoization. 

The function should take a single integer argument n and return the nth Fibonacci number. If n is less than or equal to 0, the function should return "Invalid input. Please enter a positive integer." The function should also handle non-integer inputs by either returning an error message or converting the input to an integer. 

Use a dictionary for memoization to store previously computed Fibonacci numbers in the optimized recursive solution.
"""

def fibonacci(n, memory = {}):
    """
    Compute the nth Fibonacci number using optimized recursive approach with memoization.

    Args:
    n (int): The position of the Fibonacci number to be computed.
    memory (dict, optional): Dictionary to store previously computed Fibonacci numbers. Defaults to {}.

    Returns:
    int: The nth Fibonacci number if n is a positive integer, otherwise returns an error message.
    """
    if not isinstance(n, int) or n <= 0:
        return "Invalid input. Please enter a positive integer."
    if n in memory:
        return memory[n]
    elif n == 1:
        value = 0
    elif n == 2:
        value = 1
    else:
        value = fibonacci(n-1, memory) + fibonacci(n-2, memory)
    memory[n] = value
    return value