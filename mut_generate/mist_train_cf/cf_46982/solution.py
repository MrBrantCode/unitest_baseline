"""
QUESTION:
Create a function named `fibonacci(n)` that calculates the nth Fibonacci number modulo 10^9+7 using memoization. The function should take an integer `n` as input and return the corresponding Fibonacci number. The result should be within the range of 10^9+7. The function should be efficient for large inputs by utilizing memoization to store previously calculated Fibonacci numbers.
"""

def fibonacci(n):
    MOD = (10 ** 9) + 7
    memo = {0: 0, 1: 1}
    
    if n in memo:
        return memo[n]
    
    if n % 2 == 0:
        memo[n] = (2 * fibonacci(n // 2 - 1) + fibonacci(n // 2)) * fibonacci(n // 2) % MOD
    else:        
        memo[n] = (fibonacci((n + 1) // 2) ** 2 + fibonacci((n - 1) // 2) ** 2) % MOD
        
    return memo[n]