"""
QUESTION:
Write a function called `binary_search` that uses a recursive binary search algorithm to find the index of the first occurrence of a given item in a sorted array. The function should take four parameters: a sorted array `arr`, the low index `low`, the high index `high`, and the item to search for `item`. The function should return the index of the first occurrence of the item if found, or -1 if not found. The time complexity of the function should be O(log n).
"""

def binary_search(arr, low, high, item):
    if high >= low:
        mid = low + (high - low) // 2

        # Check if the mid element is the first occurrence of the item
        if (mid == 0 or arr[mid - 1] < item) and arr[mid] == item:
            return mid

        # If the mid element is greater than the item, search in the left half
        elif arr[mid] >= item:
            return binary_search(arr, low, mid - 1, item)

        # If the mid element is less than the item, search in the right half
        else:
            return binary_search(arr, mid + 1, high, item)

    # If the item is not found, return -1
    return -1