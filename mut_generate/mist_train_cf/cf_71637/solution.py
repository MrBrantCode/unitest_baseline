"""
QUESTION:
Write a function `map_with_error_handling` that takes a list of mixed data types as input, attempts to add 3 to each item, skips items that throw a TypeError, and returns a tuple containing a list of successfully processed items and a list of items that threw an error.
"""

def map_with_error_handling(input_list):
    successful_list = []
    error_list = []
    for i in input_list:
        try:
            successful_list.append(i + 3)
        except TypeError:
            error_list.append(i)
    return (successful_list, error_list)