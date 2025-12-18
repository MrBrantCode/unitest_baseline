"""
QUESTION:
Construct a function `sorted_prime_factors` that takes a list of integers as input and returns a list of lists, where each sublist contains the prime factors of the corresponding input number in ascending order. The function should handle non-prime numbers, 0, and 1 by returning their prime constituents and an empty list, respectively.
"""

def sorted_prime_factors(numbers):
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    result = []
    for number in numbers:
        if number < 2:
            result.append([])
        else:
            result.append(sorted(prime_factors(number)))
    return result