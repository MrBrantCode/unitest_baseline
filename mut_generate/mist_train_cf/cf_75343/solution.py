"""
QUESTION:
Write a function `is_valid_IP(strng)` that takes a string `strng` as input and returns `True` if it's a valid IP address and `False` otherwise. A valid IP address consists of exactly 4 numbers separated by periods, each number is between 0 and 255 (inclusive), and does not have leading zeroes unless the number is 0 itself.
"""

def is_valid_IP(strng):
    lst = strng.split('.')
    if len(lst) != 4:
        return False
    for num in lst:
        if not num.isdigit():
            return False
        i = int(num)
        if i < 0 or i > 255:
            return False
        if len(num) > 1 and num[0] == '0':
            return False
    return True