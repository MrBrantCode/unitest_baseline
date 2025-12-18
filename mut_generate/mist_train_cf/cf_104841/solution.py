"""
QUESTION:
Implement a function `bitwise_operations(x, y)` that takes in two integers `x` and `y` and returns a list containing their bitwise AND, OR, and XOR results. The list should be in the order: AND, OR, XOR. If the number of set bits in `x` is greater than the number of set bits in `y`, append the string "x has more set bits" to the list. If the number of set bits in `y` is greater, append the string "y has more set bits" to the list.
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

    return result