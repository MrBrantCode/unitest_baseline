"""
QUESTION:
Find the 2 smallest unique prime numbers in a list of integers. The function should have a time complexity of O(n) and use constant space. The input list may contain duplicates. Implement a function `find_smallest_primes` that takes a list of integers as input and returns the smallest and second smallest unique prime numbers found in the list.
"""

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


def find_smallest_primes(numbers):
    smallest_prime = float('inf')
    second_smallest_prime = float('inf')

    for num in numbers:
        if is_prime(num):
            if num < smallest_prime:
                second_smallest_prime = smallest_prime
                smallest_prime = num
            elif num < second_smallest_prime and num != smallest_prime:
                second_smallest_prime = num

    return smallest_prime, second_smallest_prime