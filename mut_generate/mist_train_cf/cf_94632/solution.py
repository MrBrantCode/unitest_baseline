"""
QUESTION:
Write a function called `prime_numbers` that takes two parameters, `lower_limit` and `upper_limit`, and returns a list of all prime numbers between `lower_limit` and `upper_limit` (inclusive). The function should have a time complexity of O(n * sqrt(m)), where n is the number of elements in the range and m is the average value of the range, and use a space complexity of O(n), where n is the number of prime numbers in the range.
"""

def entrance(lower_limit, upper_limit):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n**0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    primes = [num for num in range(lower_limit, upper_limit + 1) if is_prime(num)]
    return primes