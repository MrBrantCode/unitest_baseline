"""
QUESTION:
Write a function `find_pairs` that takes an array of integers `arr` and a target integer `target` as input, and returns the count of unique pairs in the array whose sum is equal to the target. The function should handle duplicate elements, negative numbers, and large input arrays, and should have a time complexity of O(n) and use constant space.
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