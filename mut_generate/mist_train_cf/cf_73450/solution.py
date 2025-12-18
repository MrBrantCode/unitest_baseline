"""
QUESTION:
Implement a function `calculate` that takes a list of integers as input and returns a string containing the mean, the number of values below, equal to, and above the mean, and the corresponding ratios. The function should handle the case where the input list is empty and other potential exceptions. The solution should be time and space efficient.
"""

def calculate(input_list):
    """
    Calculate the mean of a list of integers and the number of values below, equal to, and above the mean.

    Args:
    input_list (list): A list of integers.

    Returns:
    str: A string containing the mean, the number of values below, equal to, and above the mean, and the corresponding ratios.

    Raises:
    ZeroDivisionError: If the input list is empty.
    Exception: For any other type of exception.
    """

    try:
        # Calculate the mean of the list
        mean = sum(input_list) / len(input_list)

        # Define counters for values below, equal to, and above the mean
        below = 0
        equal = 0
        above = 0

        # Go through the list and update counters
        for i in input_list:
            if i < mean: 
                below += 1
            elif i == mean: 
                equal += 1
            else: 
                above += 1

        # Calculate the ratios
        total = below + equal + above
        ratio_below = round(below / total, 2)
        ratio_equal = round(equal / total, 2)
        ratio_above = round(above / total, 2)

        return f'Mean: {mean}, Below: {below}, Equal: {equal}, Above: {above}, Ratio: {ratio_below}:{ratio_equal}:{ratio_above}'

    except ZeroDivisionError:
        return 'The list provided is empty'

    except Exception as e:
        return str(e)