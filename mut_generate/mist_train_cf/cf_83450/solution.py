"""
QUESTION:
Write a function named `max_distinct_subarray` that takes a multidimensional array of arrays as input and returns the sub-array with the maximum number of distinct elements.
"""

def max_distinct_subarray(multi_array):
    max_distinct = 0   # Initialize the maximum distinct elements counter
    max_subarray = []  # Initialize the sub-array with the most distinct elements
    for subarray in multi_array:
        distinct = len(set(subarray))  # Calculate the number of distinct elements in the subarray
        if distinct > max_distinct:    # If this number is higher than the the maximum counter 
            max_distinct = distinct    # Assign it as the maximum
            max_subarray = subarray    # Update the sub-array
    return max_subarray