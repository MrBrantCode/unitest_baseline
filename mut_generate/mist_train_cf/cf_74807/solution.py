"""
QUESTION:
Create a Python function `decimal_to_ternary` that takes two parameters, `start` and `end`, representing a range of decimal numbers. The function should convert each number in the range to its ternary representation and store the results in a dictionary where the keys are the original decimal numbers and the values are the corresponding ternary representations. The function should return this dictionary. The function should handle the case where `start` or `end` is 0.
"""

def decimal_to_ternary(start, end):
    ternary_dict = {}
    for decimal in range(start, end + 1):
        if decimal == 0:
            ternary_dict[decimal] = '0'
        else:
            ternary = ''
            temp = decimal
            while temp > 0:
                ternary = str(temp % 3) + ternary
                temp //= 3
            ternary_dict[decimal] = ternary

    return ternary_dict