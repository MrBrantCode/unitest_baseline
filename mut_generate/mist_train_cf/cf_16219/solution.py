"""
QUESTION:
Create a function named `group_by_prime` that takes a list of integers as input and returns a dictionary with two keys: 'positive' and 'negative'. Group the prime numbers from the input list into their respective keys in the dictionary, ignoring non-prime numbers and using the absolute value of each number to determine primality. The function should handle both positive and negative integers.
"""

def group_by_prime(numbers):
    primes_dict = {}
    for num in numbers:
        if all(num % i != 0 for i in range(2, int(abs(num)**0.5) + 1)) and abs(num) > 1:
            sign = 'positive' if num > 0 else 'negative'
            primes_dict.setdefault(sign, []).append(num)
    return primes_dict