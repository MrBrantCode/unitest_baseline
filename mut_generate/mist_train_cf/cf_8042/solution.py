"""
QUESTION:
Create a function `factorial(n)` to calculate the factorial of a given integer `n` using a for loop, without using the multiplication operator (`*`) or any built-in factorial functions. The function should handle edge cases, including negative numbers and large numbers that may cause overflow. The goal is to minimize the number of iterations while maintaining efficiency in terms of time and space complexity. The function should return the calculated factorial value or an error message if the input is invalid.
"""

def factorial(n):
    """
    Calculate the factorial of a given integer n without using the multiplication operator.

    Args:
    n (int): The input number.

    Returns:
    int or str: The calculated factorial value or an error message if the input is invalid.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = result + result  # (i - 1) times
        for _ in range(i - 2):
            result = result + result
    
    return result