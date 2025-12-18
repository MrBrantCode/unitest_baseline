"""
QUESTION:
Write a function `find_max_prime_subarray(array, k)` that calculates the maximum sum of a subarray of length `k` that consists only of prime numbers in the given `array`. The function should return the maximum sum found. If no such subarray exists, return 0. The function should use a helper function `is_prime(num)` to check if a number is prime. The `is_prime(num)` function should return `True` if the number is prime, and `False` otherwise.
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
        subarray_sum = sum(subarray)
        if all(is_prime(num) for num in subarray) and subarray_sum > max_sum:
            max_sum = subarray_sum
    return max_sum