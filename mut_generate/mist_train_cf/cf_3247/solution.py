"""
QUESTION:
Create a function called `factorial` that calculates the factorial of a given number using dynamic programming. The function should store the calculated values in an array to avoid redundant calculations. The function should return the correct factorial value, handling potential indexing errors and avoiding out-of-range access. The input to the function is a non-negative integer `n`. The function should return the factorial of `n`.
"""

def factorial(n):
    if n == 0:
        return 1
    
    dp = [0] * (n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        dp[i] = i * dp[i-1]
    
    return dp[n]