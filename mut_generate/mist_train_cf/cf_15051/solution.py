"""
QUESTION:
Write a function `find_pairs(arr, target)` that takes an array `arr` of integers and an integer `target` as input and returns the count of unique pairs of elements in the array whose sum is equal to the target. The function should handle duplicate elements in the array, have a time complexity of O(n), and use a hash table.
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