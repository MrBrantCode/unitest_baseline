"""
QUESTION:
Implement the function `bitwise_product(a, b)` that takes two integers `a` and `b` as arguments and returns their product without using the multiplication operator, bitwise shift operators (`<<` and `>>`), and the bitwise AND operator (`&`). You can only use the bitwise OR (`|`), bitwise XOR (`^`), and bitwise NOT (`~`) operators.
"""

def bitwise_product(a, b):
    if a == 0 or b == 0:
        return 0

    # Calculate the absolute values of a and b
    abs_a = abs(a)
    abs_b = abs(b)

    # Determine the sign of the product
    sign = 1
    if a < 0 and b < 0:
        sign = 1
    elif a < 0 or b < 0:
        sign = -1

    result = 0

    # Perform bitwise multiplication
    while abs_a != 0:
        if abs_a % 2 == 1:
            result = result ^ abs_b
        abs_a = (abs_a + (~0)) // 2
        abs_b = abs_b + abs_b

    # Adjust the sign of the result
    if sign == -1:
        result = (~result) + 1

    return result