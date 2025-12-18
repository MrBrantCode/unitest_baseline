"""
QUESTION:
Write a function `merge_sort(strings)` that sorts a list of strings in reverse alphabetical order while ignoring case differences and maintaining stability. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions or libraries.
"""

def merge_sort(strings):
    # Base case: if the list has only one element, return it
    if len(strings) <= 1:
        return strings

    # Split the list into two halves
    mid = len(strings) // 2
    left = strings[:mid]
    right = strings[mid:]

    # Recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves while maintaining stability
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Compare the strings while ignoring case
        if left[i].lower() > right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements from the left and right halves
    result.extend(left[i:])
    result.extend(right[j:])

    return result