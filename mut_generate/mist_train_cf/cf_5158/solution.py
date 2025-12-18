"""
QUESTION:
Write a function named `fibonacci` that calculates the nth Fibonacci number using recursion. The function should maintain a cache of previously calculated Fibonacci numbers to optimize performance and achieve a time complexity of O(n). The function should take two parameters: `n` and an optional dictionary `cache` with a default value of an empty dictionary.
"""

def fibonacci(n, cache={}):
    """
    Calculate the nth Fibonacci number using recursion with memoization.

    Args:
        n (int): The position of the Fibonacci number to calculate.
        cache (dict, optional): A dictionary to store previously calculated Fibonacci numbers. Defaults to {}.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
        cache[n] = result
        return result