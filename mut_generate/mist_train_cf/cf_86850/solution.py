"""
QUESTION:
Create a function named `group_primes` that takes a list of integers as input, groups the prime numbers into a dictionary where each prime number is a key and its value is a list of its occurrences, and returns the dictionary. The function should ignore non-prime numbers and consider the sign of each prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def group_primes(numbers):
    primes_dict = {}
    for num in numbers:
        if is_prime(abs(num)):
            if num in primes_dict:
                primes_dict[num].append(num)
            else:
                primes_dict[num] = [num]
    return primes_dict