"""
QUESTION:
Design a Python function, `binary_insertion_sort`, that performs a binary search-based insertion sort on a list of integers. The function should be able to sort the list in either ascending or descending order, handle duplicate numbers, and perform the operation recursively.
"""

def binary_insertion_sort(arr, desc=False):
    def binary_search(arr, val, start, end):
        # this function finds the position of val within arr to keep arr sorted
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start+1
        elif start > end:
            return start

        mid = (start+end)//2
        if arr[mid] < val:
            return binary_search(arr, val, mid+1, end)
        elif arr[mid] > val:
            return binary_search(arr, val, start, mid-1)
        else:
            return mid

    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr[::-1] if desc else arr