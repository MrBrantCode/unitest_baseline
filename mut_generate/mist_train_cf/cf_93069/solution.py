"""
QUESTION:
Write a function `second_largest_prime` that takes an array of integers as input and returns the second-largest prime number in the array. If no such number exists, return -1. Assume the input array contains at least one integer.
"""

def second_largest_prime(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = -1
    second_largest_prime = -1
    
    for num in arr:
        if is_prime(num):
            if num > largest_prime:
                second_largest_prime = largest_prime
                largest_prime = num
            elif num > second_largest_prime and num != largest_prime:
                second_largest_prime = num
    
    return second_largest_prime