"""
QUESTION:
Implement a function named `merge_sort` that takes an array of elements as input. The function should sort the array in ascending order using the Merge Sort algorithm and return the sorted array along with the total number of merge operations performed. The function should be able to handle arrays containing both numbers and strings, sorting them independently in lexicographic order for strings and numerical order for numbers. If the array contains both data types, the function should place numbers before strings. The function should not assume any order relation between elements of different data types.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_count = merge_sort(arr[:mid])
    right, right_count = merge_sort(arr[mid:])
    merged, merge_count = merge(left, right)

    return merged, left_count + right_count + merge_count

def merge(left, right):
    merged = []
    merge_operations = 0
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if isinstance(left[left_index], str) and isinstance(right[right_index], str):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        elif isinstance(left[left_index], (int, float)) and isinstance(right[right_index], (int, float)):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        elif isinstance(left[left_index], (int, float)):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        merge_operations += 1

    # append the remaining items, if any.
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    merge_operations += len(left[left_index:]) + len(right[right_index:])
    
    return merged, merge_operations