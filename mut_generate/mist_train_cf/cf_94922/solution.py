"""
QUESTION:
Create a function `transform_and_sort` that takes an array of integers as input, adds 5 to each element, removes duplicates, and returns the resulting array in ascending order.
"""

def transform_and_sort(input_array):
    result = []
    for num in input_array:
        result.append(num + 5)
    
    result = list(set(result))
    result.sort()
    
    return result