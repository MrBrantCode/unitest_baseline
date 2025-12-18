"""
QUESTION:
Write a function `find_next_primes(num, count)` that takes an integer `num` and an integer `count` as input and returns the first `count` prime numbers after `num`. The function should not use any external libraries or pre-built functions for checking prime numbers and should optimize the prime number checking algorithm to achieve a time complexity of O(n√m) for checking if a number is prime.
"""

def find_next_primes(num, count):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        sqrt_n = int(n**0.5) + 1
        for i in range(5, sqrt_n + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    primes = []
    next_num = num + 1

    while len(primes) < count:
        if is_prime(next_num):
            primes.append(next_num)
        next_num += 1

    return primes