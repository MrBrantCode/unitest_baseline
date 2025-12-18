"""
QUESTION:
Write a function `count_distinct_elements(numbers_list)` that takes a non-empty list of integers as input and returns the number of distinct elements in the list. The function should have a time complexity of O(n) and should not use any built-in Python functions or libraries that directly solve the problem, such as set() or Counter(). It should also not use additional data structures such as dictionaries or sets. The function should use a sorting algorithm to determine the distinct elements and should not modify the input list.
"""

def count_distinct_elements(numbers_list):
    # Sort the list in ascending order
    numbers_list = merge_sort(numbers_list)

    # Initialize a count variable and set it to 1
    count = 1

    # Iterate through the sorted list and count the distinct elements
    for i in range(1, len(numbers_list)):
        if numbers_list[i] != numbers_list[i-1]:
            count += 1

    return count

# Merge sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged