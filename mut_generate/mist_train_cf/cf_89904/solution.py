"""
QUESTION:
Write a function `find_max_prime_subarray(array, k)` that calculates the maximum sum of a subarray of length `k` that consists only of prime numbers in the given `array`. If no such subarray exists, return 0. The function should return the maximum sum found. Assume that `array` is a list of integers and `k` is a positive integer.
"""

def find_max_prime_subarray(array, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_sum = 0
    for i in range(len(array) - k + 1):
        subarray = array[i:i+k]
        if all(is_prime(num) for num in subarray):
            max_sum = max(max_sum, sum(subarray))
    return max_sum