"""
QUESTION:
Write a function `find_smallest_primes(lst)` that finds the two smallest unique prime numbers in a given list of integers. The function should not use any built-in prime number checking functions or libraries. The solution should have a time complexity of O(n) and use constant space. The input list may contain duplicates.
"""

def find_smallest_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

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