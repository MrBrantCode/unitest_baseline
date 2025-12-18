"""
QUESTION:
Implement a function named `reverse_ternary_search` that takes a reversely sorted array `arr` and a key to search for. The function should return the index of the key in the array if found, and -1 otherwise. The time complexity of the function should be O(log3(n)) and space complexity should be O(1), where n is the number of elements in the array.
"""

def reverse_ternary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle1 = left + (right - left) // 3
        middle2 = right - (right - left) // 3

        if arr[middle1] == key:
            return middle1
        if arr[middle2] == key:
            return middle2

        if key > arr[middle1]:
            right = middle1 - 1
        elif key < arr[middle2]:
            left = middle2 + 1
        else:
            left = middle1 + 1
            right = middle2 - 1

    return -1