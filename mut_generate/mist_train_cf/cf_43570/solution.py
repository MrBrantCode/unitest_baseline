"""
QUESTION:
Implement a function `check_and_output` that takes a list of three integers as input, identifies the prime and composite numbers in the list, and outputs the smallest prime and smallest composite number. If the list does not contain any prime or composite numbers, the function should alert the user. The function should use a helper function `check_prime` that checks whether a given number is prime or not. The input numbers are whole numbers (positive, zero, or negative) and the function should handle all possible inputs.
"""

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def check_and_output(numbers):
    primes = [num for num in numbers if check_prime(num)]
    composites = [num for num in numbers if not check_prime(num)]
    if primes:
        print('Smallest Prime: ', min(primes))
    else:
        print('No Prime number in the set.')
    if composites:
        print('Smallest Composite: ', min(composites))
    else:
        print('No Composite number in the set.')