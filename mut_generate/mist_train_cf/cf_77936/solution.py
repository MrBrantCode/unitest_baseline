"""
QUESTION:
Write a function called `primesLessThanInFibonacci` that takes an integer `n` as input and returns a list of prime numbers less than `n` that are also Fibonacci numbers. The function should use a sieve algorithm to generate prime numbers and a generator to generate Fibonacci numbers. The output list should be in ascending order. The function should not include any prime numbers greater than or equal to `n`.
"""

def primesLessThanInFibonacci(n):
    # Creating an array of booleans of length n+1
    sieve = [True] * (n + 1)
    for k in range(2, int(n ** 0.5) + 1):
        if sieve[k]:
            for i in range(k * k, n + 1, k):
                sieve[i] = False
    primes = {p for p in range(2, n) if sieve[p]}

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