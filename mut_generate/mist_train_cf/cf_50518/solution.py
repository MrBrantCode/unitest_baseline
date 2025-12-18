"""
QUESTION:
Implement the `merge_sort` function using the Divide-and-Conquer algorithm to sort a list of numbers in ascending order. The function should take a list of numbers as input and return a new sorted list. The solution should have a time complexity of O(n log n) and a space complexity of O(n), where n is the number of elements in the input list.
"""

def merge_sort(input_array):
    if len(input_array) <= 1:  # base case
        return input_array

    # Divide list into two sublists, sort them, and merge them
    mid = len(input_array) // 2
    left_half = merge_sort(input_array[:mid])
    right_half = merge_sort(input_array[mid:])

    return merge(left_half, right_half)


def merge(left, right):  
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If left list is larger
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # If right list is larger
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged