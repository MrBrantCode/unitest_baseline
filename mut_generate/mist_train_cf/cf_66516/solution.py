"""
QUESTION:
Write a Python function named `compute` that takes two parameters, `val1` and `val2`, and returns a tuple. The first element of the tuple should be either the string "Higher" if `val1` multiplied by 2 is greater than `val2`, or the integer 0 otherwise. The second element of the tuple should be `val1` multiplied by 2. The function should handle cases where `val1` or `val2` are not numbers.
"""

def compute(val1, val2):
    if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
        if val1 * 2 > val2:
            result = "Higher"
        else:
            result = 0
        return result, val1 * 2
    else:
        return 'Error: Both values should be numbers.'