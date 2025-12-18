"""
QUESTION:
Write a function `group_primes(numbers)` that takes a list of integers `numbers` as input, groups the prime numbers into a dictionary where the keys are the prime numbers and the values are lists of the same prime number repeated as many times as it appears in the input list, ignoring non-prime numbers.
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