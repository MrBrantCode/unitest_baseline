"""
QUESTION:
Create a function called `prime_divisors(n)` that takes a number `n` up to 10^12 as input and returns a list of its prime divisors in ascending order. If the number `n` is prime, the function should return an empty list. The function should have a time complexity of O(sqrt(n) * log(log(n))).
"""

import math

def prime_divisors(n):
    prime_divisors_list = []

    for i in range(2, int(math.sqrt(n)) + 1):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and n % i == 0:
            prime_divisors_list.append(i)
            while n % i == 0:
                n /= i

    if n > 1:
        return []
    else:
        return prime_divisors_list