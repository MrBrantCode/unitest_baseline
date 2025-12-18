"""
QUESTION:
Write a function named `fibMemo` that takes a positive integer `n` and a dictionary `memo` as input. The function should return the `n`th element of the Fibonacci sequence, where `n` is less than or equal to 50. Use memoization to optimize the function by storing previously calculated Fibonacci values in the `memo` dictionary, initialized with `memo[1] = 0` and `memo[2] = 1`. If `n` is less than or equal to 0 or greater than 50, return an error message.
"""

def fibMemo(n, memo):
    if n <= 0 or n > 50:
        return "Error: n should be a positive integer less than or equal to 50."
    
    if n in memo:
        return memo[n]
    
    if n == 1:
        memo[1] = 0
        return 0
    elif n == 2:
        memo[2] = 1
        return 1
    
    memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]