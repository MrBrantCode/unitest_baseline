"""
QUESTION:
Remove all duplicates from the given array of positive integers in-place and sort the remaining unique elements in descending order. The function should modify the original array and return the new length of the array. The solution must be implemented in linear time complexity without using any additional data structures, such as sets or dictionaries. The input array will contain only positive integers.
"""

def entrance(arr):
    arr.sort()
    i = 0
    for j in range(len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    new_length = i + 1
    arr[:new_length] = arr[:new_length][::-1]
    return new_length