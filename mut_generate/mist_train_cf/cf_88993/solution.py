"""
QUESTION:
Design a function `sum_of_squares(n, memo={})` to calculate the sum of squares of numbers between 1 and n. The function should handle negative input values by converting them to positive, check for non-integer inputs and return an error message, and utilize memoization to store previously calculated results. The function should run in O(log(n)) time complexity.
"""

def sum_of_squares(n, memo={}):
    # Check if n is not an integer
    if not isinstance(n, int):
        return "Error: Input value must be an integer."

    # Convert negative n to positive
    n = abs(n)

    # Check if n is zero or a decimal number
    if n == 0 or n != int(n):
        return "Error: Input value must be a positive integer."

    # Check if result is already memoized
    if n in memo:
        return memo[n]

    # Base case: n = 1
    if n == 1:
        memo[n] = 1
        return 1

    # Recursive case: sum of squares of numbers between 1 and n
    # Calculate the sum of squares of numbers between 1 and (n-1)
    # and add n^2 to the result
    result = sum_of_squares(n - 1, memo) + n**2

    # Memoize the result
    memo[n] = result

    return result