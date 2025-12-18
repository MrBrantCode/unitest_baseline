"""
QUESTION:
Write a function `print_primes_in_range` that prints the first 10 prime numbers in a given range (inclusive). The function should take two parameters: `start` and `end`, which define the range of numbers to check. Do not use any built-in prime checking functions or libraries.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
            count += 1
            if count == 10:
                break