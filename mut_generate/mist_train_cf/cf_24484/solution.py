"""
QUESTION:
Write a function `get_prime_numbers(start, end)` that returns a list of prime numbers within the given range from `start` to `end` (inclusive). A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def get_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers