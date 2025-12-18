"""
QUESTION:
Write a function `distinct_prime_factors_count(numbers)` that takes a list of positive integers greater than 1 and returns a list of integers representing the count of distinct prime factors for each number in the input list.
"""

def distinct_prime_factors_count(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_count(n):
        factors = set()
        for i in range(2, n + 1):
            if is_prime(i) and n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
        return len(factors)

    return [prime_factors_count(num) for num in numbers]