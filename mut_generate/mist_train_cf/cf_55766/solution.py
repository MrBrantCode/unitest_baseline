"""
QUESTION:
Write a function named `match_parens` that takes a list of two strings, each consisting only of open parentheses '(' and close parentheses ')'. Return 'Yes' if the strings can be concatenated in some order to form a string with properly nested parentheses, and 'No' otherwise. The strings may contain nested parentheses.
"""

def match_parens(lst):
    """
    This function checks if two strings of parentheses can be concatenated in some order to form a string with properly nested parentheses.

    Args:
        lst (list): A list of two strings, each consisting only of open parentheses '(' and close parentheses ')'.

    Returns:
        str: 'Yes' if the strings can be concatenated in some order to form a string with properly nested parentheses, 'No' otherwise.
    """

    lst1, lst2 = lst

    open_count_1 = lst1.count('(')
    close_count_1 = lst1.count(')')

    open_count_2 = lst2.count('(')
    close_count_2 = lst2.count(')')

    if open_count_1 < close_count_1 and open_count_2 > close_count_2:
        return 'Yes'
    elif open_count_1 > close_count_1 and open_count_2 < close_count_2:
        return 'Yes'
    elif open_count_1 == close_count_1 and open_count_1 + open_count_2 == close_count_1 + close_count_2:
        return 'Yes'
    else:
        return 'No'