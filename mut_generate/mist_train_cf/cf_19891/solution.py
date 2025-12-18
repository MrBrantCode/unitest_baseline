"""
QUESTION:
Create a function named `find_prime_sum` that takes a list of integers as input and returns the first three elements in the list whose sum is a prime number. The function should return `None` if no such triplet is found.
"""

def find_prime_sum(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                total = nums[i] + nums[j] + nums[k]
                if is_prime(total):
                    return [nums[i], nums[j], nums[k]]
    return None