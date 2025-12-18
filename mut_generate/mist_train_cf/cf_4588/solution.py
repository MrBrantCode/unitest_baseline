"""
QUESTION:
Write a function `find_unique_elements` that returns the unique elements in the input array in the same order as they appear, using only constant space and with a time complexity of O(n^2).
"""

def find_unique_elements(arr):
    unique_elements = []
    n = len(arr)

    for i in range(n):
        is_unique = True
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                is_unique = False
                break
        if is_unique:
            unique_elements.append(arr[i])

    return unique_elements