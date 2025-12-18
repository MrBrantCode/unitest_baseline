"""
QUESTION:
Write a function called `sum_of_squares_tuple` that takes a tuple and a list as parameters. The function should calculate the sum of squares of each integer in the tuple, including those in nested and deeply nested tuples, and append the results to the list. If the tuple is empty, the function should return an error message. The function should also return distinct error messages for non-integer inputs, negative integers, and tuples with nesting levels exceeding three.
"""

def sum_of_squares_tuple(tup, lst, level=1):
    if len(tup) == 0:
        return "Error: Empty tuple"
        
    if level > 3:
        return "Error: Too deeply nested tuple"
        
    for i in tup:
        if isinstance(i, tuple):
            lst = sum_of_squares_tuple(i, lst, level + 1)
            if isinstance(lst, str) and lst.startswith("Error"):
                return lst
        elif isinstance(i, int):
            if i >= 0:
                lst.append(i**2)
            else:
                return "Error: Negative number in tuple"
        else:
            return "Error: Non-integer input in tuple"
            
    return lst