"""
QUESTION:
Create a function named `odd_or_even` that takes a list of tuples as input. Each tuple contains two integers. The function should return a new list where each element is the first element of the corresponding input tuple if it's an odd number; otherwise, it's the second element of the tuple. The function must have a time complexity of O(n), where n is the number of tuples in the input list.
"""

def odd_or_even(lst):
    """
    This function takes a list of tuples as input, where each tuple contains two integers.
    It returns a new list where each element is the first element of the corresponding input tuple if it's an odd number; 
    otherwise, it's the second element of the tuple.

    Time complexity: O(n), where n is the number of tuples in the input list.

    Parameters:
    lst (list): A list of tuples, each containing two integers.

    Returns:
    list: A new list with the first element of each tuple if it's odd, otherwise the second element.
    """
    return [tup[0] if tup[0] % 2 == 1 else tup[1] for tup in lst]