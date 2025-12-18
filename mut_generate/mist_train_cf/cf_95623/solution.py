"""
QUESTION:
Write a function `find_pairs(nums, k)` that determines if the given array `nums` contains exactly two distinct pairs of numbers that add up to the given number `k`. The array `nums` may contain duplicates and negative numbers, and each pair of numbers must consist of one positive number and one negative number.
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