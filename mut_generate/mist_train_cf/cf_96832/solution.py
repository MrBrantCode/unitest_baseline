"""
QUESTION:
Write a function `find_max_prime_subarray` that takes two parameters: an array of integers and an integer k. The function should return the maximum sum of a subarray of length k that consists only of prime numbers. If there are not enough prime numbers in the array to form a subarray of length k, return 0.
"""

def find_max_prime_subarray(nums, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in nums if is_prime(num)]

    if len(primes) < k:
        return 0

    max_sum = current_sum = sum(primes[:k])
    for i in range(k, len(primes)):
        current_sum = current_sum - primes[i-k] + primes[i]
        max_sum = max(max_sum, current_sum)

    return max_sum