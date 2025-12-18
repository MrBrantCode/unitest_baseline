"""
QUESTION:
Implement the function find_median(sequence) that takes a list of integers as input and returns the median value of the sequence without using any built-in sorting functions or data structures. The function should correctly handle both odd and even length sequences.
"""

def find_median(sequence):
    sorted_nums = []
    for num in sequence:
        pos = 0
        while pos < len(sorted_nums) and num > sorted_nums[pos]:
            pos += 1
        sorted_nums.insert(pos, num)
    
    length = len(sorted_nums)
    if length % 2 == 1:
        median = sorted_nums[length // 2]
    else:
        median = (sorted_nums[length // 2] + sorted_nums[(length // 2) - 1]) / 2
    
    return median