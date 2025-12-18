"""
QUESTION:
Write a function `combine_and_sort(arr1, arr2)` that takes two non-empty lists of integers as input, combines them into one, sorts the resultant list in ascending order, and then transforms this list into a string delineated by commas. The function should work for both positive and negative integers, as well as zero. Implement appropriate error handling to ensure that both inputs are lists and all elements are integers.
"""

def combine_and_sort(arr1, arr2):
    
    if isinstance(arr1, list) and isinstance(arr2, list): # check if both inputs are lists
        for i in arr1: # check if all elements in arr1 are integers
            if not isinstance(i, int):
                return "All elements of the first array must be integers."
        for i in arr2: # check if all elements in arr2 are integers
            if not isinstance(i, int):
                return "All elements of the second array must be integers."

        combined_arr = arr1 + arr2 # combine the two arrays
        combined_arr.sort() # sort the combined array in ascending order
        return ",".join(str(i) for i in combined_arr) # transform the sorted array into a string delineated by commas
    else:
        return "Both inputs must be lists." # if either of the inputs is not a list