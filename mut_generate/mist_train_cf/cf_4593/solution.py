"""
QUESTION:
Write a function named `find_kth_prime_fibonacci` that takes two parameters, `k` and `N`, where `k` is the position of the prime Fibonacci number to be found and `N` is a large number used for prime checking. The function should return the k-th prime Fibonacci number. The function should be efficient and optimized for large values of `N`.
"""

def find_kth_prime_fibonacci(k, N):
    # Function to check if a number is prime using the Sieve of Eratosthenes
    def is_prime(n):
        if n <= 1:
            return False
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        return sieve[n]

    count = 0
    fib1, fib2 = 1, 1
    while count < k:
        fib = fib1 + fib2
        if is_prime(fib):
            count += 1
            if count == k:
                return fib
        fib1, fib2 = fib2, fib
    return "Error: Unable to find the k-th prime Fibonacci number"