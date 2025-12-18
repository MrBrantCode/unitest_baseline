"""
QUESTION:
Create a function called `factorial` that calculates the factorial of a given non-negative integer. The function should use recursion, handle cases where the input is not an integer or is negative, and avoid exceeding Python's maximum recursion depth. The function should have a default second parameter `result` with a value of 1.
"""

def factorial(n, result=1):
    # check if the input is an integer
    if not isinstance(n, int):
        return "Error: Input is not an integer"

    # check if the input is a negative integer
    if n < 0:
        return "Error: Input must be a non-negative integer"

    # base case
    if n == 0 or n == 1:
        return result

    # recursive case
    else:
        return factorial(n-1, n*result)