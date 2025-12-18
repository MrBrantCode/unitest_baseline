"""
QUESTION:
Design a function called `sort_data` that can sort extensive and voluminous data sets effectively, considering both time complexity and space complexity. The function should be able to handle large data sets and should have a time complexity of at least O(n log n) in the average and worst-case scenario.
"""

def sort_data(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left_half = sort_data(data[:mid])
    right_half = sort_data(data[mid:])
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
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged