"""
QUESTION:
Implement a function `find_pairs(arr, target)` that takes an array of integers and a target sum as input, and returns the count of unique pairs in the array whose sum is equal to the target. The function should have a time complexity of O(n) and use constant space, where n is the length of the array. The function should handle duplicate elements, negative numbers, and find all pairs whose sum is equal to the target.
"""

def find_pairs(arr, target):
    count = 0
    hash_table = {}

    for num in arr:
        complement = target - num

        if complement in hash_table:
            count += hash_table[complement]

        if num in hash_table:
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    return count