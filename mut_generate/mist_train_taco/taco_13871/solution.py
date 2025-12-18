"""
QUESTION:
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true.
Given num = 5, return false.


Follow up: Could you solve it without loops/recursion?

Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases.
"""

def is_power_of_four(num: int) -> bool:
    """
    Check if the given integer is a power of 4.

    Parameters:
    num (int): The integer to check.

    Returns:
    bool: True if the number is a power of 4, False otherwise.
    """
    return num != 0 and num & (num - 1) == 0 and (num & 1431655765 == num)