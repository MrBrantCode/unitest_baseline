"""
QUESTION:
Create a function `fibonacci_and_primes(n)` that calculates the Fibonacci sequence up to `n` elements and identifies all prime numbers within the sequence. The function should not use any library functions specific to Fibonacci calculation or prime number identification.
"""

def fibonacci_and_primes(n):
    fib = [0, 1] 
    primes = [] 

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    for i in range(2, n):
        next = fib[i - 1] + fib[i - 2]
        fib.append(next)

    for num in fib:
        if is_prime(num):
            primes.append(num)

    return fib, primes