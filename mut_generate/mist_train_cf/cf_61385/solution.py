"""
QUESTION:
Write a function named `find_second_third_least` that takes a numerical array `arr` as input and returns the second and third least values in ascending order. The function should handle cases where the array has fewer than 3 unique elements.
"""

def find_second_third_least(arr):
    # check if the number of elements less than 3
    if len(arr) < 3:
        return "The given array does not have enough elements"
    
    # sort the array in ascending order
    sorted_array = sorted(arr)
    
    # remove duplicates
    unique_array = list(set(sorted_array))
    
    # check if the number of unique elements less than 3
    if len(unique_array) < 3:
        return "The given array does not have enough unique elements"
    
    # return the second and third elements as they are second and third least now
    return unique_array[1], unique_array[2]