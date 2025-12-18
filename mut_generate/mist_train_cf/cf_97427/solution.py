"""
QUESTION:
Write a function `replace_value` that takes a sorted list of tuples (key-value pairs), a key, and a value as input. Replace the value of the given key with the new value using a binary search algorithm with a time complexity of O(log n), where n is the number of key-value pairs. If the key is not found, return None. The list of tuples is already sorted in ascending order based on the keys. Do not use any built-in Python functions or libraries for sorting or searching.
"""

def replace_value(dictionary, key, value):
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

    index = binary_search(dictionary, key)

    if index != -1:
        dictionary[index] = (key, value)
        return dictionary

    return None