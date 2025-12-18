"""
QUESTION:
Find the index of the last occurrence of a given item in an array. The solution should be implemented without using built-in functions or libraries that directly solve the problem and without using any additional data structures. The function should return the index of the last occurrence of the item if found, and -1 if not found.

The function should be named `last_index` and should take two parameters: the array and the item to be searched.
"""

def last_index(arr, item):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == item:
            return i
    return -1