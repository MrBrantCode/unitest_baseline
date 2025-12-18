"""
QUESTION:
Write a function `dictionary_keys_sort(dictionary)` that takes a dictionary as input and returns a list of its keys sorted in ascending order. The function should run in O(n log n) time complexity, where n is the number of keys in the dictionary. Do not use any built-in sorting functions or methods to sort the dictionary keys; instead, implement a sorting algorithm using key comparisons and swaps.
"""

def dictionary_keys_sort(dictionary):
    keys = list(dictionary.keys())
    n = len(keys)
    
    # Implementing bubble sort algorithm
    for i in range(n-1):
        for j in range(0, n-i-1):
            if keys[j] > keys[j+1]:
                keys[j], keys[j+1] = keys[j+1], keys[j]
    
    return keys