"""
QUESTION:
Create a function `problem_solution(my_string)` that takes a string `my_string` as input and replaces all prime numbers in the string with their square values. The function should return the modified string. The prime numbers and their indexes in the string should be identified using a Regular Expression pattern.
"""

import re

def is_prime(n):
    """Check if integer n is a prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5)+1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True

def problem_solution(my_string):
    numbers = re.findall('\d+', my_string)
    indexes = [m.start() for m in re.finditer('\d+', my_string)]
    primes = [val if is_prime(int(val)) else False for val in numbers]
    prime_indexes = [index for index, val in zip(indexes, primes) if val]
    squared_primes = [str(int(val)**2) if val else False for val in primes]
    squared_primes = list(reversed(squared_primes))
    prime_indexes = list(reversed(prime_indexes))
    for index, val in zip(prime_indexes, squared_primes):
        if val:
            pre = my_string[:index]
            post = my_string[index:]
            post = re.sub('\d+', val, post, 1)
            my_string = pre+post
    return my_string