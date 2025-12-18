"""
QUESTION:
Create a function called `catalan` that calculates the nth Catalan number, where n is a positive integer, using memoization. The function should return the calculated Catalan number. If n is not a positive integer, the function should return an error message.

Create another function called `catalan_range` that calculates a list of Catalan numbers within a specified range, from start to end, where both start and end are positive integers. The function should return a list of calculated Catalan numbers. If the range is invalid (i.e., end is less than start) or if start or end is not a positive integer, the function should return an error message.
"""

def catalan(n, memo = {0:1, 1:1}):
    # if result is already in memory, return it
    if n in memo:
        return memo[n]
    # check if given number is integer and positive
    elif not isinstance(n, int) or n < 0 :
        return "Error: the input value must be a positive integer."
    else:
        # calculate the Catalan number
        result = 0
        for i in range(n):
            result += catalan(i) * catalan(n-i-1)
        memo[n] = result
        return result


def catalan_range(start, end):
    # Check if the range is valid
    if end < start:
        return "Error: end should be larger than start."
    elif not (isinstance(start, int) and isinstance(end, int)) or start < 0 or end < 0:
        return "Error: the start and end values must be positive integers."
    else:
        return [catalan(n) for n in range(start, end+1)]