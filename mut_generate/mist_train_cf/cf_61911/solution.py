"""
QUESTION:
Create a function `find_prime_sequence()` that takes no arguments. This function should find a unique 12-digit numerical entity that can be constructed by concatenating the three terms present in a sequence of 4-digit prime numbers that form an arithmetic progression. The sequence should be distinct from 1487, 4817, 8147. The function should return the 12-digit numerical entity as a string. 

The 4-digit prime numbers should form an arithmetic progression, meaning the difference between any two successive members is a constant. Additionally, the 4-digit numbers should be permutations of each other.
"""

import itertools

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def find_prime_sequence():
    primes = [num for num in range(1001, 10000, 2) if is_prime(num)]
    
    for prime in primes:
        checked_seq = sorted([int(''.join(num)) for num in set(itertools.permutations(str(prime), len(str(prime)))) if int(''.join(num)) in primes])
        for i in range(len(checked_seq) - 2):
            if checked_seq[i+2] - checked_seq[i+1] == checked_seq[i+1] - checked_seq[i]:
                sequence = str(checked_seq[i]) + str(checked_seq[i+1]) + str(checked_seq[i+2])
                if sequence != '148748178147':
                    return sequence
    return None