"""
QUESTION:
Write a function named `invert_list` that takes a list as input and returns a new list that is the reverse of the input list without modifying the original list. The function should accept a list as a parameter and return a list as output.
"""

def invert_list(input_list):
    """
    This function takes a list as an input and returns a new list that is an inverted version of the input list. 
    It does not modify the original list.

    :param input_list: Original list to be inverted.
    :type input_list: list
    :return: Inverted list (a duplicate of the original list in reverse order).
    :rtype: list
    """

    # the ::-1 indexing operation creates a reverse copy of list
    inverted_list = input_list[::-1]

    return inverted_list