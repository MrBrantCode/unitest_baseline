"""
QUESTION:
Write a function named `find_differences` that takes a list of integers as input. The function should return a list of differences between each pair of successive numbers in the input list. If the input is not a list or if the list contains non-integer values, the function should return an error message.
"""

def find_differences(array):
    if not isinstance(array, list):
        return 'Invalid data type, should be list.'
        
    try:
        differences = [array[i+1] - array[i] for i in range(len(array)-1)]
        return differences
    except (TypeError, IndexError):
        return 'The list should contain only integers.'