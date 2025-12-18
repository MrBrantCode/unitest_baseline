"""
QUESTION:
Create a function called `multiply_list_by_scalar` that takes three parameters: a list of integers, a scalar value, and a boolean value. The function should multiply each integer in the list by the scalar value if the boolean value is True and return the result as a new list. If the boolean value is False, the function should return the original list unchanged.
"""

def multiply_list_by_scalar(lst, scalar, should_multiply):
    if not should_multiply:
        return lst
    multiplied_lst = []
    for num in lst:
        multiplied_lst.append(num * scalar)
    return multiplied_lst