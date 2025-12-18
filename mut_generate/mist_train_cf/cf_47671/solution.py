"""
QUESTION:
Create a function named `my_function` that takes two sets of two numerical inputs as arguments. The function should subtract the second number from the first in each set and then multiply the results of both sets. The function must handle potential edge cases, such as invalid inputs or exceptional mathematical conditions. The inputs are valid if they are lists or tuples containing exactly two integers or floating-point numbers.
"""

def my_function(set1, set2):
    # check if the inputs are valid sets of two numbers
    if not (isinstance(set1, (list, tuple)) and len(set1) == 2 and all(isinstance(i, (int, float)) for i in set1)) \
            or not (isinstance(set2, (list, tuple)) and len(set2) == 2 and all(isinstance(i, (int, float)) for i in set2)):
        return "Error: Invalid input. Each input set must contain two numbers."

    # handle exceptional mathematical cases
    if set1[0] - set1[1] == 0 or set2[0] - set2[1] == 0:
        return 0

    # subtract second number from the first in each set and then multiply the results
    result = (set1[0] - set1[1]) * (set2[0] - set2[1])

    return result