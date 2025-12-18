"""
QUESTION:
Write a function `fibonacci_upto_n` that generates a list of Fibonacci numbers up to a given limit `n`. The function should use memoization to optimize performance and handle large `n` values without exceeding Python's recursion limit.
"""

def fibonacci_upto_n(n):
    memo = {0: 0, 1: 1}
    fiblist = []
    i = 0
    
    while True:
        fib_i = memo.get(i, None)
        if fib_i is None:
            fib_i = memo[i-1] + memo[i-2]
            memo[i] = fib_i
        
        if fib_i > n:
            break
        fiblist.append(fib_i)
        i += 1
    return fiblist