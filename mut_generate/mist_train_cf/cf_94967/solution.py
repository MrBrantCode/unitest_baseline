"""
QUESTION:
Create a function called `recursive_sort` that takes an array as input and returns a new array with the elements sorted in descending order using a recursive sorting algorithm with a time complexity of O(nlogn).
"""

def recursive_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left_sorted = recursive_sort(left)
    right_sorted = recursive_sort(right)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from both arrays and add the larger one to the merged array
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add the remaining elements from left or right array
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged