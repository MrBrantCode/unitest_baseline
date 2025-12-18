"""
QUESTION:
Create a function `factorial(n, memo={})` that calculates the factorial of a positive integer `n` using recursion and memoization. The function should handle edge cases such as negative integers and non-integer inputs, returning an error message if the input is invalid. Implement the function with a time complexity of O(n) and a space complexity of O(n).
"""

def factorial(n, memo={}):
    # Check if n is a positive integer
    if not isinstance(n, int) or n < 0:
        return "Invalid input. Please enter a positive integer."

    # Check if n is already calculated
    if n in memo:
        return memo[n]

    # Base case: factorial of 0 is 1
    if n == 0:
        return 1

    # Recursive case: calculate factorial using memoization
    result = n * factorial(n-1, memo)
    memo[n] = result
    return result