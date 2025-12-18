"""
QUESTION:
Develop a function named `convert_to_integers` that takes an array of values as input and returns a new array where each real number is converted to its nearest integer. The conversion should round up if the decimal part is greater than 0.5 and round down otherwise. If the input array contains any non-numeric values, the function should instead return an error message listing the non-numeric values. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def convert_to_integers(arr):
    """
    This function takes an array of values as input, converts real numbers to their nearest integer,
    and returns a new array. It rounds up if the decimal part is greater than 0.5 and rounds down otherwise.
    If the input array contains any non-numeric values, it returns an error message listing the non-numeric values.

    Args:
        arr (list): A list of values.

    Returns:
        list: A new list with real numbers converted to integers, or an error message if non-numeric values are found.
    """
    result = []
    non_numeric_values = []
    
    for num in arr:
        if isinstance(num, (int, float)):
            result.append(round(num))
        else:
            non_numeric_values.append(str(num))
    
    if non_numeric_values:
        return "Error: The following values are non-numeric - " + ", ".join(non_numeric_values)
    
    return result