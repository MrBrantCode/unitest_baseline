"""
QUESTION:
Implement the function `remove_duplicates_and_sort(arr)` that takes a list of integers as input, removes duplicates, and sorts the list in ascending order. The function should handle potential exceptions, including an empty list and a list that is already sorted. The sorting algorithm used should have a time complexity of O(n log n) on average.
"""

def remove_duplicates_and_sort(arr):
    try:
        # check if list is empty
        if len(arr) == 0:
            return []
        # check if list is already sorted
        if arr == sorted(arr):
            return arr
    
        # remove duplicate using a dictionary
        arr = list(dict.fromkeys(arr))
    
        # sort the array
        arr.sort()
        return arr
    except Exception as e:
        print ("An error occurred: ", e)