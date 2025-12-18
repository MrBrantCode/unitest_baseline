"""
QUESTION:
Write a recursive function `print_primes` that takes an integer `n` and prints all prime numbers from 1 to `n` in reverse order, separated by a semicolon. The function should utilize the Sieve of Eratosthenes algorithm to find the primes and print them without any additional characters at the beginning or end of the output, except for the semicolons separating the numbers.
"""

def print_primes(n):
    def sieve_of_eratosthenes(n):
        primes = [True for i in range(n+1)]
        p = 2
        while p * p <= n:
            if primes[p] == True:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n+1) if primes[p]]

    def print_primes_recursive(n, primes):
        if n < 2:
            return
        if primes and primes[-1] == n:
            print(n, end='')
            primes.pop()
        else:
            print_primes_recursive(n-1, primes)
            return
        if n != 2:
            print(';', end='')
        print_primes_recursive(n-1, primes)

    primes = sieve_of_eratosthenes(n)[::-1]
    print_primes_recursive(n, primes)