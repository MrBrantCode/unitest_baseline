"""
QUESTION:
Design a function `find_prime_indices` that takes an array of positive integers as input and returns a dictionary where the keys are the prime numbers in the array and the values are their indices of the first and last occurrence.
"""

def find_prime_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_indices = {}
    for i, num in enumerate(nums):
        if is_prime(num):
            if num not in prime_indices:
                prime_indices[num] = [i, i]
            else:
                prime_indices[num][1] = i
    return prime_indices