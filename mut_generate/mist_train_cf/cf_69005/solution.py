"""
QUESTION:
Write a function `fib(n: int, a: int, b: int)` that implements a specialized version of the Fibonacci sequence. The function should take two initial values `a` and `b`, and an index `n`, and return the `n`-th value in the sequence. If `a` is odd, the function should handle negative indices differently. If `n` is less than 0 and `a` is odd, the function should return an error message. If `b` is an even number greater than 10, the function should return a modified value. Use dynamic programming to calculate the `n`-th value in the sequence.
"""

def fib(n: int, a: int, b: int):
    if a % 2 != 0:  
        if n < 0:
            return "Cannot use negative indices with this value of a"
        elif n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return 1
    else:  
        if n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return 1
        if n < 0:
            if b > 10 and b % 2 == 0:  
                return a + b - n 
    
    dp = [0 for _ in range(n+1)]
    dp[0] = a
    dp[1] = b
    dp[2] = 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]