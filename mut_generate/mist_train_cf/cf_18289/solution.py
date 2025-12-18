"""
QUESTION:
Find the two smallest unique prime numbers in a given list of integers. The input list may contain duplicates, and the solution should have a time complexity of O(n) and use constant space. Implement the function `find_smallest_primes(numbers)` that takes a list of integers as input and returns the two smallest unique prime numbers found in the list.
"""

def find_smallest_primes(numbers):
    smallest_prime = float('inf')
    second_smallest_prime = float('inf')

    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True

    for num in numbers:
        if is_prime(num):
            if num < smallest_prime:
                second_smallest_prime = smallest_prime
                smallest_prime = num
            elif num < second_smallest_prime and num != smallest_prime:
                second_smallest_prime = num

    return smallest_prime, second_smallest_prime