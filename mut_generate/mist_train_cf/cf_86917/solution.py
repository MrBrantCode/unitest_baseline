"""
QUESTION:
Write a function named `count_and_sum_primes` that takes a list of numbers as input and returns a tuple containing two values: the number of unique prime numbers in the list and the sum of all the unique prime numbers in the list. The function should ignore non-integer, negative, and floating-point values, as well as duplicates, and return (0, 0) if the input list is empty. The function should be optimized for large input lists.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_and_sum_primes(lst):
    primes = set()
    prime_sum = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num not in primes:
            if is_prime(num):
                primes.add(num)
                prime_sum += num
    return len(primes), prime_sum