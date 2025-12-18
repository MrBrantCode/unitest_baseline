"""
QUESTION:
Write a recursive function `recursive_sum(input_array)` that calculates the cumulative total of all numerical elements in a multi-dimensional array. The array can contain a mix of numerical elements and further sub-arrays, and the function should be able to handle array structures of various depths and configurations, including empty sub-arrays and non-numeric elements.
"""

def recursive_sum(input_array):
    """
    A function that takes a multi-dimensional array and returns
    the cumulative total of all numerical elements within the array structure.
    """
    total_sum = 0
    for element in input_array:
        # check if element is a list
        if isinstance(element, list):
            # if it's a list, call the function recursively
            total_sum += recursive_sum(element)
        elif isinstance(element, (int, float)):
            total_sum += element
        else:
            continue
    return total_sum