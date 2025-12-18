"""
QUESTION:
Create a function called `fibonacci` that generates the Fibonacci sequence up to a given positive integer `n` using an iterative approach with memoization to achieve a time complexity of O(n). The function should handle large numbers efficiently and avoid redundant calculations.
"""

def fibonacci(n):
    """
    Generates the Fibonacci sequence up to a given positive integer n using an iterative approach with memoization.
    
    Args:
        n (int): A positive integer.
    
    Returns:
        list: The Fibonacci sequence up to n.
    """
    memo = {0: 0, 1: 1}  # Initialize memo dictionary with base cases

    for i in range(2, n+1):
        # Calculate Fibonacci number and store it in memo dictionary
        memo[i] = memo[i-1] + memo[i-2]

    # Return the Fibonacci sequence as a list
    return list(memo.values())