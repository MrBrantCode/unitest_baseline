"""
QUESTION:
Create a function called `get_prime_numbers` that takes two integers `lower_limit` and `upper_limit` as input and returns a list of all prime numbers between `lower_limit` and `upper_limit` (inclusive). The function should have a time complexity of O(n * sqrt(m)) and a space complexity of O(n), where n is the number of elements in the range and m is the average value of the range.
"""

def get_prime_numbers(lower_limit, upper_limit):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for num in range(lower_limit, upper_limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes