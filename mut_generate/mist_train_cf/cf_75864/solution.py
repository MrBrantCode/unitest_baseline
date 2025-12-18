"""
QUESTION:
Write a function called `remove_special_chars_and_digits` that takes a string `s` as input, removes special characters and unique digits in a case-insensitive manner, and returns the new string along with the count of each removed character or digit. 

The function should treat '.' , ',' , '&' , '7' equally to '.' , ',' , '&' , '7' regardless of where they appear in the string. The function should not consider multi-byte (non-ASCII) characters as special characters.
"""

import re

def remove_special_chars_and_digits(s):
    """
    Removes special characters and unique digits from a string in a case-insensitive manner
    and returns the new string along with the count of each removed character or digit.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing the new string and a dictionary with the count of each removed character or digit.
    """
    count_dict = {}
    new_str = re.sub(r'([\W\d])', lambda m: count_dict.update({m.group(1): count_dict.get(m.group(1), 0)+1}) or '', s)
    return new_str, count_dict