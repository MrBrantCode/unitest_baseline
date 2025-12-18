"""
QUESTION:
Implement the `sort_tuples` function to sort a list of tuples in ascending order based on the first value of the tuple. The function should have the following properties:

- The list of tuples can have up to 1 million elements.
- Each tuple can have up to 10 elements.
- Each element in the tuple can have up to 10 characters.
- The sorting algorithm used should have a time complexity of O(n log n) or better.
- The sorting algorithm should be stable, maintaining the relative order of tuples with the same first value.
- The sorting should be performed in place, manipulating the original list directly.
- The function should not use any built-in sorting functions or libraries.
"""

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def sort_tuples(lst):
    return merge_sort(lst)