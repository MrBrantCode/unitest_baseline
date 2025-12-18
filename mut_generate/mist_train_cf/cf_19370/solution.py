"""
QUESTION:
Implement a function `replace_x_with_y(lst)` that replaces all instances of the string 'x' with 'y' in the given list `lst`, maintaining the original order of elements. The list `lst` can contain a combination of integers and strings, with a maximum length of 10^6 and string lengths up to 100 characters. The replacement should be case-sensitive.
"""

def replace_x_with_y(lst):
    result = []
    for element in lst:
        if element == 'x':
            result.append('y')
        else:
            result.append(element)
    return result