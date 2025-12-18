"""
QUESTION:
Write a Python function named `lcm` that takes a list of integers as input and returns the least common multiple (LCM) of all the numbers in the list. The function should have a time complexity of O(n log n), where n is the length of the input list.
"""

import math

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return factors

def lcm(numbers):
    primes = []
    for num in numbers:
        factors = prime_factors(num)
        for factor in factors:
            if factor not in primes:
                primes.append(factor)
    max_powers = {}
    for prime in primes:
        max_power = 0
        for num in numbers:
            power = prime_factors(num).count(prime)
            if power > max_power:
                max_power = power
        max_powers[prime] = max_power
    lcm = 1
    for prime, power in max_powers.items():
        lcm *= prime ** power
    return lcm