"""
QUESTION:
Write a function `prime_range` that takes two integers `C` and `D` as input, where `C` and `D` are both inclusive, and returns the count of twin primes within this range. The function should also print all prime numbers within the range and the average distance between consecutive prime numbers. A twin prime is a pair of prime numbers that differ by 2. The function should handle edge cases properly. Note that although recursion is not the most suitable approach for this problem, if a recursive solution is required, please specify how recursion should be applied.
"""

import math

def prime_range(C, D):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n > 2 and n % 2 == 0:
            return False

        max_div = math.floor(math.sqrt(n))
        for i in range(3, 1 + max_div, 2):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in range(C, D + 1):
        if is_prime(num):
            primes.append(num)

    twin_count = 0
    for i in range(len(primes) - 1):
        if primes[i+1] - primes[i] == 2:
            twin_count += 1
    
    distances = [primes[i+1] - primes[i] for i in range(len(primes) - 1)]
    avg_distance = sum(distances) / len(distances) if distances else 0

    print("Primes: ", primes)
    print("Number of Twin Primes: ", twin_count)
    print("Average distance: ", avg_distance)

    return twin_count