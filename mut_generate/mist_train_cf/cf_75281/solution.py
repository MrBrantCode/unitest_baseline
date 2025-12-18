"""
QUESTION:
Create a function called `sum_of_squares_tuple` that takes two parameters: a tuple `tup` and a list `lst`. The function should calculate the sum of squares of each element in the tuple, handle tuples within tuples (nested tuples), and append the results to the given list. The function should return an error message if the tuple is empty, contains non-integer inputs, or has more than three levels of nesting. It should also handle negative numbers in the tuple by returning an error message.
"""

def sum_of_squares_tuple(tup, lst, depth=0):
    if tup == ():
        return "Error: Tuple is empty"
    if depth > 3:
        return "Error: Too much nesting"
    for i in tup:
        if isinstance(i, tuple):
            result = sum_of_squares_tuple(i, lst, depth+1)
            if type(result) == str:
                return result
        else:
            if not isinstance(i, int):
                return "Error: Non-integer input in tuple"
            if i < 0:
                return "Error: Negative number in tuple"
            lst.append(i**2)
    return lst