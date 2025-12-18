"""
QUESTION:
Design a function called `fibo_primes(n)` that calculates prime Fibonacci numbers under a given number `n`. The function should optimize for time and space complexities of O(n).
"""

def fibo_primes(n):
    # Sieve of Eratosthenes
    sieve = [0, 0] + [1 for i in range(2, n+1)]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = 0
    # Fibonacci sequence
    fib = [0, 1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    # Prime Fibonacci numbers
    return [f for f in fib[2:] if sieve[f]]