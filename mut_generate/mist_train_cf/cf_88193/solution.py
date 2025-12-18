"""
QUESTION:
Write a function named `delete_duplicates` to delete all duplicate elements from the input array in-place, without using any built-in functions or methods that directly solve the problem, and without using additional data structures or arrays to store intermediate results. The function should have a time complexity of O(n), where n is the length of the array, and the order of the elements in the resulting array does not matter. The function should only use a while loop and should not raise any errors.
"""

def delete_duplicates(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            del arr[i+1]
        else:
            i += 1
    return arr