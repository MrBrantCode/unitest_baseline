"""
QUESTION:
Write a function `unique_avg(array1, array2)` that takes two arrays of integers as parameters and returns the average of all unique integers present in both arrays. Ensure the function handles cases where the arrays might be empty.
"""

def unique_avg(array1, array2):
    # convert both arrays to sets to remove duplicates within each array
    # then use set union to find unique values across both arrays
    unique_values = set(array1).union(set(array2))
    
    # check if there are any unique values
    if len(unique_values) == 0:
        return 0
    else:
        # return the average of the unique values
        return sum(unique_values) / len(unique_values)