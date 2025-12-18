"""
QUESTION:
Write a function named `max_value` that takes an array of mixed data types as input and returns the maximum numerical value. The function should not use any built-in max function or sorting methods. If the array only contains strings, return "No numerical values found."
"""

def max_value(arr):
    max_value = None
    no_numeric_values = True

    for el in arr:
        if type(el) == int or type(el) == float:
            no_numeric_values = False
            if max_value is None or el > max_value:
                max_value = el

    if no_numeric_values:
        return "No numerical values found."
    else:
        return max_value