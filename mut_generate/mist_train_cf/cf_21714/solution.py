"""
QUESTION:
Create a function named `filter_array` that takes an array of mixed data types as input and returns a new array with all integers removed. The resulting array should only contain strings and floating-point numbers. The filter should be case-sensitive, excluding any strings that start with a capital letter. The function should preserve the order of the remaining elements and should not use any built-in functions or libraries for filtering or type checking.
"""

def filter_array(arr):
    filtered_arr = []
    for element in arr:
        if type(element) == str:
            if element[0].islower():
                filtered_arr.append(element)
        elif type(element) == float:
            filtered_arr.append(element)
    return filtered_arr