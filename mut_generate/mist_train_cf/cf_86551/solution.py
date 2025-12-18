"""
QUESTION:
Implement a function named `remove_duplicates` that takes an array of integers as input and returns the array with duplicate elements removed, preserving the original order. The function should have a time complexity of O(n^2) or less and a space complexity of O(1), without using any built-in functions or libraries for removing duplicates or additional data structures.
"""

def remove_duplicates(arr):
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Compare the current element with all the elements after it
        for j in range(i+1, len(arr)):
            # If a duplicate is found, remove it
            if arr[i] == arr[j]:
                arr.pop(j)
                break

    return arr