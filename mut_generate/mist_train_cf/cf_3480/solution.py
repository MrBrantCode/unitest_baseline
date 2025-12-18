"""
QUESTION:
Write a function `find_smallest_primes(lst)` that finds the two smallest unique prime numbers in a given list `lst` of integers. The function should have a time complexity of O(n), use constant space, and not rely on any built-in prime number checking functions or libraries. If no two unique prime numbers exist in the list, the function should return the smallest prime number and infinity, or two infinity values if no prime numbers exist.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_smallest_primes(lst):
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in lst:
        if is_prime(num):
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num < second_smallest and num != smallest:
                second_smallest = num
    
    return smallest, second_smallest