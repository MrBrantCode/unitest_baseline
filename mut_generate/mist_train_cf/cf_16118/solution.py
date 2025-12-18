"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes an array as input, removes duplicate elements while maintaining the original order of elements, and does not use any additional data structures. The function should have a time complexity of O(n^2).
"""

def entance(arr):
    # Traverse the array
    for i in range(len(arr)):
        j = i + 1
        # Compare each element with all the elements after it
        while j < len(arr):
            # If a duplicate element is found, remove it
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j += 1
    return arr