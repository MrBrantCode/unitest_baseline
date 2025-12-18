"""
QUESTION:
Create a function named `is_cyclic_rotation` that takes two non-negative integers `num1` and `num2` as input. The function should return `True` if `num1` is a cyclic rotation of `num2`, and `False` otherwise. The function should be able to handle numbers with up to 10^6 digits and minimize both time and space complexity. Note that the input numbers can contain leading zeros.
"""

def is_cyclic_rotation(num1, num2):
    # Convert the numbers to strings for easier manipulation
    str1 = str(num1)
    str2 = str(num2)
    
    # Check if the lengths of the strings are different
    if len(str1) != len(str2):
        return False
    
    # Check if str1 is a substring of str2 concatenated with itself
    return str1 in str2 + str2