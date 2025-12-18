"""
QUESTION:
Create a function named `factorial(n, memo)` that calculates the factorial of a given number `n` using recursion and memoization. The function should take two parameters: `n` (the number for which to calculate the factorial) and `memo` (a dictionary used for memoization, defaulting to an empty dictionary). Implement memoization to store and reuse previously computed results. Include comments to explain the purpose of each recursive call.
"""

def entance(n, memo = {}):
    # Base case:
    if n == 0:
        return 1
    # Checking if the result has been previously computed
    if n not in memo:
        # If the result is not in the memo, compute it by recursively calling entance(n - 1)
        memo[n] = n * entance(n - 1, memo)
    # By reaching here, we either found the result in memo, or we have computed it, so return it
    return memo[n]