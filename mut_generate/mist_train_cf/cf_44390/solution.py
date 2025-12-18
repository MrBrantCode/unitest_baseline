"""
QUESTION:
Design a function called `primeFibonacci` that takes an integer `n` as input and returns a list of prime Fibonacci numbers under `n`. The function should use the Sieve of Eratosthenes algorithm to generate prime numbers and the Fibonacci sequence. The output list should only include prime Fibonacci numbers that are less than the input number `n`.
"""

def primeFibonacci(n):
    # Sieve of Eratosthenes algorithm to generate prime numbers
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)

    # Generate Fibonacci sequence
    fibs = [0, 1]
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])

    # Find prime Fibonacci numbers under n
    prime_fibs = [x for x in fibs if x in primes]
    return prime_fibs