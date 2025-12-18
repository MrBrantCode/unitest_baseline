"""
QUESTION:
Implement a function `cross_product(v1, v2, result)` that calculates the cross product of two 3D vectors `v1` and `v2`, and returns `True` if the result matches the given `result` vector, `False` otherwise. The input vectors `v1` and `v2` are represented as lists of three real numbers, and the result is also a list of three real numbers.
"""

def cross_product(v1, v2, result):
    # Calculate the cross product of v1 and v2
    cross_result = [v1[1]*v2[2] - v1[2]*v2[1],
                    v1[2]*v2[0] - v1[0]*v2[2],
                    v1[0]*v2[1] - v1[1]*v2[0]]
    
    # Compare the calculated cross product with the expected result
    return cross_result == result