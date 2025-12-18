"""
QUESTION:
Write a function `last_occurrence(arr, num)` that finds the index of the last occurrence of `num` in the ordered list `arr` without using pre-existing Python methods. The function should return the index of the last occurrence of `num` if found, and -1 otherwise.
"""

def last_occurrence(arr, num):
    for i in range(len(arr)-1, -1, -1):    # Loop from the end to the start
        if arr[i] == num:
            return i    # Return index when match is found
    return -1   # Return -1 if element is not found