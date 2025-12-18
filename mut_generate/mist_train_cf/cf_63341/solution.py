"""
QUESTION:
Write a generator function named `prime_generator` that takes an integer `n` as input and generates prime numbers between `n^2` and `2n^2`, along with their digital root. The function should support random inputs within the range `10 ≤ n ≤ 50` without performance degradation. The digital root of a number is calculated using the formula `(n - 1) % 9 + 1` for `n > 0`.
"""

def prime_generator(n):
    def digital_root(num):
        return (num - 1) % 9 + 1 if num > 0 else 0

    primes = [True] * (2 * n * n + 1)
    p = 2
    while p*p <= 2 * n * n:
        if primes[p]==True:
            for i in range(2*p, 2 * n * n + 1, p):
                primes[i] = False
        p += 1

    for number in range(n * n, 2 * n * n + 1):
        if primes[number]:
            yield number, digital_root(number)