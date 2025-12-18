"""
QUESTION:
Design a function `find_sublists` that identifies the longest continuous sublist(s) within the given list containing both prime and Fibonacci numbers. The function should return the starting and ending indices of these sublists. The function should consider negative numbers, zero, and floating point numbers as non-prime and non-Fibonacci numbers. The function should be able to handle large lists efficiently without using external libraries for prime or Fibonacci number detection. If there are multiple sublists of the same maximum length, the function should return all of them along with their starting and ending indices.
"""

def find_sublists(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n**0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def is_fibonacci(n):
        a, b = 0, 1
        while b < n:
            a, b = b, a+b
        return b == n

    primes_fibs = [(num, i) for i, num in enumerate(lst) if isinstance(num, int) and num >= 0 and (is_prime(num) or is_fibonacci(num))]

    if not primes_fibs:
        return []

    start, end = primes_fibs[0][1], primes_fibs[0][1]
    max_length = 1
    max_sublists = [(start, end)]

    for i in range(1, len(primes_fibs)):
        if primes_fibs[i][1] - primes_fibs[i-1][1] == 1:
            end = primes_fibs[i][1]
            if end - start + 1 > max_length:
                max_length = end - start + 1
                max_sublists = [(start, end)]
            elif end - start + 1 == max_length:
                max_sublists.append((start, end))
        else:
            start, end = primes_fibs[i][1], primes_fibs[i][1]

    return max_sublists