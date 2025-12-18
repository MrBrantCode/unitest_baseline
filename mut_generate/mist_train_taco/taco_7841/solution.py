"""
QUESTION:
The written representation of a number (with 4 or more digits) can be split into three parts in various different ways. For example, the written number 1234 can be split as [1 | 2 | 34] or [1 | 23 | 4] or [12 | 3 | 4].

Given a written number, find the highest possible product from splitting it into three parts and multiplying those parts together. For example:

- product of [1 | 2 | 34] = 1 \* 2 \* 34 = 68
- product of [1 | 23 | 4] = 1 \* 23 \* 4 = 92
- product of [12 | 3 | 4] = 12 \* 3 \* 4 = 144

So maximumProductOfParts(1234) = 144

For a longer string there will be many possible different ways to split it into parts. For example, 8675309 could be split as: 

- [8 | 6 | 75309] 
- [867 | 530 | 9] 
- [8 | 67 | 5309]
- [86 | 75 | 309]

or any other option that splits the string into three parts each containing at least one digit.
"""

from functools import reduce
from operator import mul

def maximum_product_of_parts(number_str):
    """
    Calculate the highest possible product from splitting the given number string into three parts and multiplying those parts together.

    Parameters:
    number_str (str): The input number as a string.

    Returns:
    int: The highest possible product obtained by splitting the number into three parts.
    """
    max_product = 0
    length = len(number_str)
    
    for i in range(1, length - 1):
        for j in range(i + 1, length):
            part1 = int(number_str[:i])
            part2 = int(number_str[i:j])
            part3 = int(number_str[j:])
            product = part1 * part2 * part3
            if product > max_product:
                max_product = product
    
    return max_product