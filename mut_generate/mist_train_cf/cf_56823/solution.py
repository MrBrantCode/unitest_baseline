"""
QUESTION:
Develop a function named `factorial` to calculate the factorial of a given integer using recursion and memoization. The function should take an integer `n` as input and return its factorial. 

Constraints:
- Do not use built-in factorial modules or libraries.
- Implement memoization to optimize for larger inputs.
- Handle input values up to 10000 without exceeding the maximum recursion limit.
- Return an error message for non-positive integers.
- Include exception handling within the function.
"""

def factorial(n, memo={}):
    """
    Calculate the factorial of a given integer using recursion and memoization.
    
    Args:
    n (int): A positive integer.
    memo (dict): A dictionary to store computed factorials for memoization. Default is an empty dictionary.
    
    Returns:
    int: The factorial of n if n is a positive integer, otherwise an error message.
    """
    if type(n) != int or n < 0:
        return 'Error: Input should be a positive integer.'
    if n == 0:
        return 1
    if n not in memo:
        memo[n] = n * factorial(n-1, memo)
    return memo[n]