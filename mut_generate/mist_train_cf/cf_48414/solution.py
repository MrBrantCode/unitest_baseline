"""
QUESTION:
Create a function named `elementwise_modulo` that takes two tuples `t1` and `t2` of the same length as input and returns a tuple containing the element-wise modulo of corresponding elements from `t1` and `t2`. If any element in `t2` is zero, return an error message 'Error: division by zero in position i', where `i` is the index of the zero element. If `t1` and `t2` are not of the same length, return 'Error: tuples are not the same size'.
"""

def elementwise_modulo(t1, t2):
    if len(t1) != len(t2):
        return "Error: tuples are not the same size"
    else:
        result = []
        for i in range(len(t1)):
            if t2[i] == 0:
                return f"Error: division by zero in position {i}"
            else:
                result.append(t1[i] % t2[i])
        return tuple(result)