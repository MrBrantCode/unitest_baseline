"""
QUESTION:
Create a function named `sum_of_divisors` that takes three lists of integers as input, classifies each number as prime or not prime, calculates the sum of divisors for each prime number, and returns a list of tuples containing the prime numbers and their corresponding sum of divisors in descending order. 

The function should consider 1 as not prime and include the number itself in the sum of divisors.
"""

import math

def sum_of_divisors(arr1, arr2, arr3):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def sum_divisors(n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors)

    prime_numbers = [num for num in arr1 + arr2 + arr3 if is_prime(num)]
    prime_sums = {prime: sum_divisors(prime) for prime in prime_numbers}
    sorted_prime_sums = sorted(prime_sums.items(), key=lambda x: x[1], reverse=True)

    return sorted_prime_sums