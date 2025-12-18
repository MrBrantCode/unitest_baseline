"""
QUESTION:
Create a function named `solve` that takes a list of tuples as input and returns a dictionary. The function should create a dictionary where each valid tuple in the input list serves as a key, and the corresponding value is a list containing the product and sum of the tuple's elements. A valid tuple is one that contains exactly two elements, both of which are numbers (either integers or floats). The function should ignore any invalid tuples in the input list.
"""

def solve(tuples):
    result = {}
    for each_tuple in tuples:
        try:
            if isinstance(each_tuple, tuple) and len(each_tuple) == 2:
                num1, num2 = each_tuple
                if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                    result[each_tuple] = [num1 * num2, num1 + num2]
        except TypeError:
            continue
    return result