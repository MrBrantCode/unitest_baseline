"""
QUESTION:
Write a function called `categorize_numbers` that takes a list of positive integers as input. The function should categorize the numbers into three categories: prime, composite, and special-case (0 and 1), removing any duplicates and sorting the numbers in ascending order within each category. Return the prime numbers, composite numbers, and special-case numbers as three separate lists.
"""

def categorize_numbers(numbers):
    # Remove duplicates
    numbers = list(set(numbers))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    primes = sorted([num for num in numbers if num > 1 and is_prime(num)])
    composites = sorted([num for num in numbers if not is_prime(num) and num not in (0, 1)])
    special_case = sorted([num for num in numbers if num in (0, 1)])

    return primes, composites, special_case