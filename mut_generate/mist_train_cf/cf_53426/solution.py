"""
QUESTION:
Create a function `create_reciprocal_dict` that takes a list of floating-point numbers as input and returns a dictionary where each number is paired with its multiplicative reciprocal (1 divided by the number), excluding zero to prevent division by zero.
"""

def create_reciprocal_dict(float_list):
    reciprocal_dict = {}
    for float_num in float_list:
        if float_num != 0: # prevent division by zero
            reciprocal_dict[float_num] = 1 / float_num
    return reciprocal_dict