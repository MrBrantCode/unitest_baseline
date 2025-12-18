"""
QUESTION:
Create a function called `prime_divisors_sum` that takes an integer `n` as input. The function should calculate the sum of the squares of all prime divisors of `n`. If `n` itself is a prime number, the function should multiply the sum by 2. Return the calculated sum. The function should not take any other inputs besides the integer `n`.
"""

import math

def prime_divisors_sum(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime(i) and n % i == 0:
            while n % i == 0:
                n /= i
                divisors.append(i)
    if is_prime(n):
        divisors.append(n)
        return 2 * sum(map(lambda x: x**2, divisors))
    else:
        return sum(map(lambda x: x**2, divisors))