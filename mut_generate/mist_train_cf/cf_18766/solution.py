"""
QUESTION:
Implement a function called `fibonacci_counter(n)` that uses dynamic programming to calculate the nth Fibonacci number and returns a tuple containing the result and the number of times the function was called. The function should have a time complexity of O(n).
"""

def fibonacci_counter(n, memo = {}, count = [0]):
    """
    This function uses dynamic programming to calculate the nth Fibonacci number.
    It also returns the number of times the function was called.

    Args:
        n (int): The position of the Fibonacci number to be calculated.
        memo (dict): A dictionary to store previously calculated Fibonacci numbers.
        count (list): A list to store the number of function calls.

    Returns:
        tuple: A tuple containing the nth Fibonacci number and the number of function calls.
    """
    count[0] += 1
    if n <= 0:
        return 0, count[0]
    elif n == 1:
        return 1, count[0]
    elif n not in memo:
        memo[n] = fibonacci_counter(n-1, memo, count)[0] + fibonacci_counter(n-2, memo, count)[0]
    return memo[n], count[0]