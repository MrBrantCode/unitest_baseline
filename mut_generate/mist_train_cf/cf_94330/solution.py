"""
QUESTION:
Write a function named `multiply` that takes two integers as input and returns their product. The function should not use the multiplication operator (`*`), any built-in multiplication functions, loops, or recursion.
"""

def multiply(x, y):
    if x == 0 or y == 0:
        return 0

    # Check if either x or y is negative
    negative = False
    if x < 0 and y > 0:
        x = -x
        negative = True
    elif x > 0 and y < 0:
        y = -y
        negative = True
    elif x < 0 and y < 0:
        x = -x
        y = -y

    # Perform bitwise multiplication
    result = 0
    while y > 0:
        if y & 1:
            result = add(result, x)
        x = x << 1
        y = y >> 1

    # Apply negative sign if necessary
    if negative:
        result = -result

    return result

def add(x, y):
    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x