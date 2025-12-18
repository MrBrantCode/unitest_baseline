"""
QUESTION:
Given a string of characters, I want the function `findMiddle()`/`find_middle()` to return the middle number in the product of each digit in the string.

Example: 's7d8jd9' -> 7, 8, 9 -> 7\*8\*9=504, thus 0 should be returned as an integer.

Not all strings will contain digits. In this case and the case for any non-strings, return -1.

If the product has an even number of digits, return the middle two digits

Example: 1563 -> 56

NOTE: Remove leading zeros if product is even and the first digit of the two is a zero.
Example 2016 -> 1
"""

from operator import mul
from functools import reduce

def find_middle(s: str) -> int:
    # Check if the input is a string and not empty
    if not isinstance(s, str) or not s:
        return -1
    
    # Extract digits from the string
    lstDig = [int(c) for c in s if c.isnumeric()]
    
    # If no digits are found, return -1
    if not lstDig:
        return -1
    
    # Calculate the product of the digits
    prod = str(reduce(mul, lstDig))
    
    # Determine the middle index(es)
    mid_index = (len(prod) - 1) // 2
    
    # Extract the middle digit(s)
    middle_digits = prod[mid_index:-mid_index or len(prod)]
    
    # Remove leading zero if present
    if len(middle_digits) == 2 and middle_digits[0] == '0':
        middle_digits = middle_digits[1]
    
    return int(middle_digits)