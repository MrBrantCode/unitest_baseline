"""
QUESTION:
Write functions `find_by_index`, `binary_search`, and `linear_search` that locate an element in a numerical array. 

- `find_by_index` takes an array and an index as input and returns the element at that index.
- `binary_search` takes a sorted array and an element as input, and returns the index of the element if found, -1 otherwise.
- `linear_search` takes an array and an element as input, and returns the index of the element if found, -1 otherwise.

Assume that array indices are 0-based. If the element is not found, return -1.
"""

def find_by_index(array, index):
    return array[index]

def binary_search(array, element):
    low = 0
    high = len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        if array[middle] < element:
            low = middle + 1
        elif array[middle] > element:
            high = middle - 1
        else:
            return middle
    return -1

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1