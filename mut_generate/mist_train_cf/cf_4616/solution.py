"""
QUESTION:
Write a function named `replace_x_with_y` that takes a list of integers and strings as input, replaces all instances of the string 'x' with the string 'y', and returns the modified list while maintaining the order of the elements. The input list may contain duplicate elements, integers, strings, or a combination of both, and the replacement should be case-sensitive. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def entance(lst):
    for i in range(len(lst)):
        if lst[i] == 'x':
            lst[i] = 'y'
    return lst