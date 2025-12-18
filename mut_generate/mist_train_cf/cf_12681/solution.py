"""
QUESTION:
Write a function `binary_search(vector, x)` that searches for an element `x` in a sorted vector using binary search. The function should return the index of `x` if it exists in the vector, and -1 otherwise. The time complexity of the function should be O(log n), where n is the number of elements in the vector.
"""

def binary_search(vector, x):
    low = 0
    high = len(vector) - 1

    while low <= high:
        mid = (low + high) // 2

        if vector[mid] == x:
            return mid
        elif vector[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found