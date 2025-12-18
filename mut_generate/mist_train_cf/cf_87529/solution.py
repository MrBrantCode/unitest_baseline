"""
QUESTION:
Create a function named `is_prime_and_sum` that takes two integers `start` and `end` as input, representing a range of numbers. The function should calculate and return the sum of all prime numbers within the given range, including `start` and `end` if they are prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime_and_sum(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(start, end+1):
        if is_prime(num):
            prime_sum += num

    return prime_sum