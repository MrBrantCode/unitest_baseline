"""
QUESTION:
Write a function `find_pairs(arr, target)` that finds all pairs in an array whose sum is equal to a given target. The function should handle duplicate elements, negative numbers, and large input arrays, and it should return the count of unique pairs found. The function should have a time complexity of O(n), where n is the length of the array, and it should use constant space.
"""

def find_pairs(arr, target):
    count = 0
    pairs = set()
    seen = set()
    
    for num in arr:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.add(pair)
        seen.add(num)
    
    count = len(pairs)
    return count