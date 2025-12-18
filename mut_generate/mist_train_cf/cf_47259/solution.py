"""
QUESTION:
Create a function `primesLessThanInFibonacci(n)` that returns an array of all prime numbers in the Fibonacci sequence that are less than the supplied integer `n`. The function should take an integer `n` as input and return a list of prime Fibonacci numbers less than `n`.
"""

def primesLessThanInFibonacci(n):
    # Creating an array of booleans of length n+1
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]: 
            for i in range(x*x, n+1, x): 
                sieve[i] = False 
    primes = [p for p in range(2, n) if sieve[p]]
    
    # Creating a generator for Fibonacci sequence
    def fib():
        a, b = 0, 1
        while True: 
            yield a
            a, b = b, a + b

    fibs = fib()
    fib_nums = []
    curr_fib = next(fibs)
    
    while curr_fib < n:
        fib_nums.append(curr_fib)
        curr_fib = next(fibs)
        
    # Return prime numbers from Fibonacci sequence
    return [num for num in fib_nums if num in primes]