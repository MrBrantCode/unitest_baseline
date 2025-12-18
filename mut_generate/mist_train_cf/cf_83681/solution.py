"""
QUESTION:
Develop a function named `add_without_plus_operator` that takes two integers `x` and `y` as input and returns their sum without using the '+' operator. The function should utilize bitwise operations to calculate the sum. The integers `x` and `y` can be any valid integer values.
"""

def add_without_plus_operator(x, y):
    """
    This function calculates the sum of two integers without using the '+' operator.
    
    It utilizes bitwise operations to achieve this. The function works by first 
    calculating the "carry" which contains all the places where both x and y have 
    a '1'. Then, it computes the sum without considering carry (using XOR). 
    Lastly, it left shifts carry. This process is repeated in a loop until there 
    is no carry, which means there are no '1's in same positions in x and y.

    Args:
        x (int): The first integer.
        y (int): The second integer.

    Returns:
        int: The sum of x and y.
    """

    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x