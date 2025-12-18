"""
QUESTION:
Write a function called `find_pairs` that takes an array `arr` of integers and a target integer `target` as input, and returns the count of unique pairs of integers in `arr` that add up to `target`. The function should handle duplicate elements in `arr` and have a time complexity of O(n), where n is the length of `arr`.
"""

def find_pairs(arr, target):
    count = 0
    pairs = set()
    hash_table = {}

    for num in arr:
        complement = target - num
        if complement in hash_table:
            pair = (min(num, complement), max(num, complement))
            if pair not in pairs:
                count += 1
                pairs.add(pair)
        hash_table[num] = True

    return count