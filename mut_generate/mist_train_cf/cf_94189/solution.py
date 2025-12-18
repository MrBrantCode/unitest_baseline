"""
QUESTION:
Write a function named `count_prime_numbers` that takes a list of numbers as input and returns a tuple containing two values: the number of unique prime numbers in the list and the sum of these prime numbers. The function should ignore non-integer and negative values in the list. If the input list is empty or contains no prime numbers, the function should return (0, 0).
"""

def count_prime_numbers(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = set()
    prime_sum = 0
    
    for num in lst:
        if isinstance(num, int) and num > 0:
            if is_prime(num):
                primes.add(num)
                prime_sum += num
    
    return len(primes), prime_sum