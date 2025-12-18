"""
QUESTION:
Implement a function named `find_pair_divisible_by_10(arr)` that takes an array of integers as input and checks if the sum of any two integers in the array is divisible by 10. The function should return the indices of the pair of integers whose sum is divisible by 10. If multiple pairs exist, it can return the indices of any valid pair. If no such pair exists, it should return an empty array.
"""

def find_pair_divisible_by_10(arr):
    remainder_dict = {}

    for i, num in enumerate(arr):
        remainder = num % 10
        complement = (10 - remainder) % 10

        if complement in remainder_dict:
            return [remainder_dict[complement][0], i]

        if remainder not in remainder_dict:
            remainder_dict[remainder] = []
        remainder_dict[remainder].append(i)

    return []