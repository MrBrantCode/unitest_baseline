"""
QUESTION:
Write a function `first_repeating_element` that takes an array of integers as input and returns the first repeating element along with its index. The function should have a time complexity of O(n) where n is the length of the array. The array can have up to 10^5 elements and the integers in the array can range from -10^3 to 10^3, inclusive. If no repeating element is found, return None for both element and index.
"""

def first_repeating_element(arr):
    hash_set = set()
    for i, num in enumerate(arr):
        if num in hash_set:
            return num, i
        else:
            hash_set.add(num)
    return None, None