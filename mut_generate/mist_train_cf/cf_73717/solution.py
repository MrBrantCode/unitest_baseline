"""
QUESTION:
Implement a function named `merge_sort` to sort a set of strings containing alphabetical characters and digits (0-9) in dictionary order, considering digits and alphabet in the order 0 < 1 < 2 < ... < 9 < A < B < ... < Z < a < b < ... < z. The function should maintain the original order of duplicate entries and not use built-in sorting functions. The length of each string is at least 1 and up to 100 characters.
"""

def merge_sort(arr):
    def rank(s):
        # Convert string to list of ordinal values of each character
        # Python's built-in `ord` function gives ASCII value, which ranks digits and alphabet as required
        return [ord(c) for c in s]

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        # Repeatedly pick smallest element from left or right half
        while left_index < len(left) and right_index < len(right):
            if rank(left[left_index]) <= rank(right[right_index]):
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Add remaining elements from either half (if any)
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged

    if len(arr) <= 1:
        return arr    # Base case

    # Recursively split array in half until we have arrays of size one
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge sorted halves
    return merge(left_half, right_half)