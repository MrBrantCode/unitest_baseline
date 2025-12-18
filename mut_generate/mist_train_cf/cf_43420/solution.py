"""
QUESTION:
Write a function `nearest_number(num_list, target)` that finds the nearest whole number to a given target number within a given numerical sequence. The function should handle fractional numbers in the series and be resistant to potential exceptions such as an empty list input or non-numeric elements in the list. The function should return a string error message if the input list is empty, the target number is not a valid number, or the input is not a list. If the input list contains non-numeric elements, the function should catch the TypeError and return a string error message.
"""

def entrance(num_list, target):
    try:
        if len(num_list) == 0:
            # Check if the input list is empty
            return "Input list is empty"
        # In case if target isn't of type int or float
        elif isinstance(target, int) == False and isinstance(target, float) == False:
            return "Target number is not valid"
        # In case if num_list isn't of type list
        elif isinstance(num_list, list) == False:
            return "Input is not a list"
        return min(num_list, key = lambda x: abs(x - target))
    except TypeError:
        return "Input list contains non-numeric elements"