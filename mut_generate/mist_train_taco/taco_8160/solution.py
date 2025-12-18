"""
QUESTION:
Given a positive integer num, write a function which returns True if num is a perfect square else False.


Note: Do not use any built-in library function such as sqrt.


Example 1:

Input: 16
Returns: True



Example 2:

Input: 14
Returns: False



Credits:Special thanks to @elmirap for adding this problem and creating all test cases.
"""

def is_perfect_square(num: int) -> bool:
    """
    Determines if a given positive integer is a perfect square.

    Parameters:
    num (int): The positive integer to check.

    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    if num < 0:
        return False
    
    # Using the property of perfect squares
    # A number is a perfect square if it can be expressed as (i * i) for some integer i
    i = 0
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False