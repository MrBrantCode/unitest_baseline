"""
QUESTION:
Write a function `find_pairs` that takes an array `nums` and a number `k` as input, and returns `True` if the array contains exactly two distinct pairs of numbers that add up to `k`, and `False` otherwise. The array may contain duplicates and negative numbers, and each pair of numbers must consist of one positive number and one negative number.
"""

def find_pairs(nums, k):
    pairs = set()
    count = 0
    
    for num in nums:
        if -num in pairs:
            pairs.remove(-num)
            count += 1
        else:
            pairs.add(num)
    
    return count == 2