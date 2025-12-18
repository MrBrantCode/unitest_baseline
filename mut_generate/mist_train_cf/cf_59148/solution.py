"""
QUESTION:
Create a function `replace_primes_with_cubes` that takes a list of integers as input, replaces each prime number with its cube, and returns the modified list. Assume that the input list contains only integers.
"""

def replace_primes_with_cubes(nums):
    def is_prime(num):
        if num <= 1:
            return False
        
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    return [num ** 3 if is_prime(num) else num for num in nums]