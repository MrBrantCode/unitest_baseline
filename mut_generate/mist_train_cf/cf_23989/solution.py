"""
QUESTION:
Create a function called `generate_prime_numbers(n)` that generates the first n prime numbers, where n is a positive integer. The function should return a list of the first n prime numbers.
"""

def generate_prime_numbers(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_nums = []
    i = 2
    while len(prime_nums) < n:
        if is_prime(i):
            prime_nums.append(i)
        i += 1
    return prime_nums