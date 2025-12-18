"""
QUESTION:
Given a list of positive integers, write a function called `remove_duplicates` that removes all duplicates from the list in-place and sorts the remaining unique elements in descending order. The function should modify the original list and return the new length of the list. The solution should be implemented in linear time complexity without using any additional data structures such as sets or dictionaries.
"""

def remove_duplicates(arr):
    arr.sort()
    i = 0
    for j in range(len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    new_length = i + 1
    arr[:new_length] = arr[:new_length][::-1]
    return new_length