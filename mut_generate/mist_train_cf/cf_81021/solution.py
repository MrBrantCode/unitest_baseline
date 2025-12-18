"""
QUESTION:
Write a function `modify_strings` that takes two strings `first_string` and `second_string` as input. The function should return a string where all characters from `second_string` are removed from `first_string` and the remaining characters are sorted in reverse lexicographical order.
"""

def modify_strings(first_string, second_string):
    # remove any characters from the first string present in the second string
    for char in second_string:
        first_string = first_string.replace(char, '')
    
    # convert to list
    str_list = list(first_string)

    # sort in lexicographical order
    str_list.sort()

    # reverse the list for reverse lexicographical order
    str_list.reverse()

    # convert list to string and return
    return "".join(str_list)