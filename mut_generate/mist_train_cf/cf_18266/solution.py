"""
QUESTION:
Write a function `count_prime_pairs` that takes an array of positive integers as input and returns the count of pairs in the array whose absolute difference is a prime number. The time complexity of the algorithm should be O(n^2), where n is the length of the input array.
"""

def count_prime_pairs(nums):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if is_prime(abs(nums[i] - nums[j])):
                count += 1
    return count