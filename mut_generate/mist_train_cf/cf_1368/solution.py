"""
QUESTION:
Write a function `count_and_sum_primes` that takes a list of numbers as input and returns a tuple containing two values: the number of unique prime numbers in the list and the sum of these prime numbers. The function should ignore non-integer, negative, and floating-point values in the list. If the input list is empty or does not contain any prime numbers, the function should return (0, 0).
"""

def count_and_sum_primes(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = set()
    prime_sum = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num not in primes:
            if is_prime(num):
                primes.add(num)
                prime_sum += num
    return len(primes), prime_sum