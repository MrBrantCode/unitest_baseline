"""
QUESTION:
Implement the `search_in_sorted_array` function to search for a target number in a sorted array, which may contain duplicate elements, and return the index of the first occurrence of the target number. The function should have a time complexity of O(log n), and it should be able to handle arrays sorted in descending order. The array may be extremely large and cannot fit in memory all at once, but for the purpose of this function, you can assume the entire array is in memory. If the target number is not found, the function should return -1. 

The function should take the following parameters: `target`, `start`, `end`, and `is_descending`. The `target` is the number to be searched, `start` and `end` are the start and end indices of the array, and `is_descending` is a boolean flag indicating whether the array is sorted in descending order.
"""

def search_in_sorted_array(array, target, start, end, is_descending):
    # Check if the array is sorted in descending order
    if is_descending:
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                # Find the first occurrence of the target number
                while mid > start and array[mid - 1] == target:
                    mid -= 1
                return mid
            elif array[mid] < target:
                end = mid - 1
            else:
                start = mid + 1
    else:
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                # Find the first occurrence of the target number
                while mid > start and array[mid - 1] == target:
                    mid -= 1
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

    # Target number not found in the array
    return -1