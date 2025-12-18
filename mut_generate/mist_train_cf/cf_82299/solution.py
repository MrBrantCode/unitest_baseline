"""
QUESTION:
Write a function named `count_pairs_with_sum` that takes an array `arr` and a target sum `sum` as input, and returns the number of pairs of elements in the array that add up to the given sum. The function should have a time complexity of O(n) and should be able to handle duplicate elements in the array. The array can contain any integers (positive, negative, or zero).
"""

def count_pairs_with_sum(arr, sum):
    hashmap = dict()
    count = 0
    for num in arr:
        if (sum - num) in hashmap:
            count += hashmap[sum - num]
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    return count