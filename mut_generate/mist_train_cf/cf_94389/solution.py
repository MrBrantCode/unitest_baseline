"""
QUESTION:
Write a function `find_median(sequence)` that calculates the median of a given sequence of numbers without using any built-in sorting functions or data structures. The sequence may contain an even or odd number of elements. If the sequence has an odd length, the median is the middle value. If the sequence has an even length, the median is the average of the two middle values.
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
        median = (sorted_nums[length // 2 - 1] + sorted_nums[length // 2]) / 2
    
    return median