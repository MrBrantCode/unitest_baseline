"""
QUESTION:
Write a function `mode` that takes a list of integers as input and returns the mode (the element that appears most frequently) in its original order of appearance. If there are multiple modes, return all of them in the order of their first appearance. The function should not reorder the input list. The function should handle lists with elements that appear once, twice, or multiple times.
"""

def entrance(nums):
    counts = dict()
    max_count = 0
    modes = []
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
        if counts[num] > max_count:
            max_count = counts[num]
            modes = [num]
        elif counts[num] == max_count and num not in modes:
            modes.append(num)
    return modes[0] if len(modes) == 1 else modes