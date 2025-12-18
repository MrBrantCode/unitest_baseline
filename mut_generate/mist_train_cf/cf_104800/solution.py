"""
QUESTION:
Create a function `get_prime_numbers` that generates a list of prime numbers from 1 to a given upper limit. The function should take an integer `n` as input, where `n` represents the upper limit, and return a list of prime numbers from 1 to `n`. For example, `get_prime_numbers(100)` should return a list of prime numbers from 1 to 100. The function should only consider integers greater than 1 as potential prime numbers.
"""

def get_prime_numbers(n):
    """Generates a list of prime numbers from 1 to a given upper limit."""
    prime_numbers = []
    for num in range(1, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers