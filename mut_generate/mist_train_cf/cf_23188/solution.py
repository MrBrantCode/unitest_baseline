"""
QUESTION:
Construct a function `find_pairs(arr, target)` to find all pairs of elements in an array whose sum equals a given target. The function should return the count of unique pairs and handle duplicate elements in the array. Implement this function with the following restrictions: constant space complexity, no built-in functions or libraries, ability to handle negative numbers, and a time complexity of O(n), where n is the length of the array.
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