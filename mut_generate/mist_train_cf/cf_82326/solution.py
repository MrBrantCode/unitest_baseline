"""
QUESTION:
Create a function named `remove_and_reduce_spaces` that takes a string as input and returns a string where all leading and trailing whitespaces are removed and multiple consecutive whitespaces are reduced to a single whitespace. The function should not use Python's built-in string functions such as `strip()` or `split()`.
"""

def remove_and_reduce_spaces(myStr):
    new_str = ''
    space_count = 0
    for ch in myStr:
        if ch != ' ':
            if space_count != 0:
                new_str += ' '
                space_count = 0
            new_str += ch
        else:
            space_count += 1
    return new_str