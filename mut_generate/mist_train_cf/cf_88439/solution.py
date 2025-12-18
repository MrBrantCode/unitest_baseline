"""
QUESTION:
Implement a function called `find_first_occurrence` that takes a sorted array of non-negative integers and floats, and a target item as input, and returns the index of the first occurrence of the target item using a recursive binary search algorithm with a time complexity of O(log n). The array may contain duplicate values and up to 10^6 elements. If the item is not found, return -1.
"""

def find_first_occurrence(arr, item):
    def binary_search(low, high):
        if high >= low:
            mid = low + (high - low) // 2

            # Check if the mid element is the first occurrence of the item
            if (mid == 0 or arr[mid - 1] < item) and arr[mid] == item:
                return mid

            # If the mid element is greater than the item, search in the left half
            elif arr[mid] >= item:
                return binary_search(low, mid - 1)

            # If the mid element is less than the item, search in the right half
            else:
                return binary_search(mid + 1, high)

        # If the item is not found, return -1
        return -1

    return binary_search(0, len(arr) - 1)