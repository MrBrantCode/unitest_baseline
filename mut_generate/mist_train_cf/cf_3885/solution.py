"""
QUESTION:
Write a function called `delete_duplicates` that takes an array as input, deletes all duplicate elements in the array in-place, and returns the modified array. The function should not use any built-in functions or methods that directly solve the problem, should have a time complexity of O(n), should not use additional data structures or arrays to store intermediate results, and should use a while loop.
"""

def delete_duplicates(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            del arr[i+1]
        else:
            i += 1
    return arr