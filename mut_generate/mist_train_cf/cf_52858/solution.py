"""
QUESTION:
Create a recursive function named `factorial` that calculates the factorial of a given number. The function should use memoization to improve efficiency and handle negative inputs by returning an error message. The function should take two parameters: `num` (the number for which the factorial is to be calculated) and `memo` (a dictionary used for memoization, defaulting to an empty dictionary).
"""

def factorial(num, memo = {}):
    if num < 0:
        return "Error, negative input"
    if num == 0:
        return 1
    elif num in memo:
        return memo[num]
    else:
        result = num * factorial(num - 1, memo)
        memo[num] = result
        return result