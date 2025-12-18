"""
QUESTION:
Write a function `replace_value` to replace the value at a given key in a sorted dictionary with a time complexity of O(log n) for the search and replacement operation. The dictionary is sorted in ascending order based on the keys and is represented as a list of tuples. The function should not use any built-in Python functions or libraries for sorting or searching. If the key is found, return the updated dictionary; otherwise, return None.

The function should take three parameters: a sorted dictionary, a key, and a value. The dictionary is a list of tuples where each tuple contains a key-value pair. The key and value are the new key and value to be replaced in the dictionary.
"""

def binary_search(dictionary, key):
    left = 0
    right = len(dictionary) - 1

    while left <= right:
        mid = (left + right) // 2

        if dictionary[mid][0] == key:
            return mid
        elif dictionary[mid][0] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def replace_value(dictionary, key, value):
    index = binary_search(dictionary, key)

    if index != -1:
        dictionary[index] = (key, value)
        return dictionary

    return None