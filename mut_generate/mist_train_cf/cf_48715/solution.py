"""
QUESTION:
Write a function `average_2d_list` that calculates the average of all values in a 2D list of integers with varying row lengths. The function must handle input errors, including non-2D list inputs and empty lists, and return an error message in these cases. The function should not use any external libraries.
"""

def average_2d_list(lst):
    try:
        return sum(sum(sub_list) for sub_list in lst) / sum(len(sub_list) for sub_list in lst)
    except TypeError:
        return "Error: Argument must be a 2D list of integers"
    except ZeroDivisionError:
        return "Error: Empty list"
    except:
        return "Error: An unexpected error occurred"