"""
QUESTION:
Write a function named `find_sum_of_primes` that takes a list of integers and returns the sum of all prime numbers in the list without using any built-in sum function, loops, or external libraries/modules.
"""

def find_sum_of_primes(nums, index):
    if index == len(nums):
        return 0
    current_num = nums[index]
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if is_prime(current_num):
        return current_num + find_sum_of_primes(nums, index + 1)
    else:
        return find_sum_of_primes(nums, index + 1)