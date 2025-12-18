"""
QUESTION:
Implement a function called `bitwise_operations` that takes two integers `x` and `y` as input. The function should return a list containing the results of the bitwise AND, OR, and XOR operations between `x` and `y`, in that order. Additionally, the function should compare the number of set bits in `x` and `y` and append a string to the list indicating which integer has more set bits, if any.
"""

def bitwise_operations(x, y):
    result = []
    result.append(x & y)  # Bitwise AND
    result.append(x | y)  # Bitwise OR
    result.append(x ^ y)  # Bitwise XOR

    count_x = bin(x).count('1')
    count_y = bin(y).count('1')

    if count_x > count_y:
        result.append("x has more set bits")
    elif count_y > count_x:
        result.append("y has more set bits")
    else:
        result.append("x and y have the same number of set bits")

    return result