"""
QUESTION:
Write a function named `find_square_pairs` that takes a list of positive integers `nums`, and a range defined by `lower` and `upper` bounds. The function should find the total count of non-overlapping pairs of adjacent numbers within the range whose product is a perfect square, and return the count along with the specific pairs. The function should be efficient enough to handle large inputs.
"""

import math

def is_perfect_square(n):
    return math.isqrt(n)**2 == n

def find_square_pairs(nums, lower, upper):
    count = 0
    pairs = []
    i = 0
    while i < len(nums) - 1:
        for j in range(i + 1, min(i + upper + 1, len(nums))):
            if lower <= nums[i] * nums[j] <= upper:
                if is_perfect_square(nums[i] * nums[j]):
                    count += 1
                    pairs.append((nums[i], nums[j]))
                    i = j  # Move to the next non-overlapping pair
                    break
        else:
            i += 1  # Increment i only if no pair is found
    return count, pairs