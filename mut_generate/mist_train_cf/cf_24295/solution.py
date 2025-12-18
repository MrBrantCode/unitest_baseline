"""
QUESTION:
Write a function `find_substring` that takes a list of strings (`lst`) and a target string (`query`) as input. The function should return a list of strings from `lst` that contain `query` as a substring.
"""

def find_substring(lst, query):
    """
    Returns a list of strings from `lst` that contain `query` as a substring.

    Parameters:
    lst (list): A list of strings.
    query (str): The target substring.

    Returns:
    list: A list of strings containing the target substring.
    """
    return [el for el in lst if query in el]