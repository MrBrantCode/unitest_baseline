"""
QUESTION:
Create a function named `prime_array` that takes an array of integers as input and returns a new array containing only the prime numbers from the original array.
"""

def prime_array(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
        
    return [num for num in nums if is_prime(num)]