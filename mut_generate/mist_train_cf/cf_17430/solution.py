"""
QUESTION:
Write a function `find_pairs` that takes a list of integers `nums` and a target sum as input, and returns all unique pairs of numbers in the list whose sum is equal to the target sum. The function should return the pairs in ascending order based on the first element of each pair, with no duplicate pairs and no pairs containing the same element twice.
"""

def find_pairs(nums, target_sum):
    pairs = set()
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in nums:
        difference = target_sum - num
        if difference in count and count[difference] > 0:
            pairs.add((min(num, difference), max(num, difference)))
            count[difference] -= 1

    return sorted(pairs, key=lambda x: x[0])