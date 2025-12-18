"""
QUESTION:
Write a function `is_single_bit_toggle_possible(str1, str2)` that takes two binary strings of the same length as input and returns `True` if the first string can be transformed into the second by toggling exactly one bit, and `False` otherwise. The function should compare the input strings bit by bit and return `False` as soon as it finds more than one difference between the strings.
"""

def entance(str1, str2):
    if len(str1) != len(str2):
        return False  

    number_of_diffs = 0  
    for bit1, bit2 in zip(str1, str2):
        if bit1 != bit2:
            number_of_diffs += 1
        if number_of_diffs > 1:  
            return False

    return number_of_diffs == 1