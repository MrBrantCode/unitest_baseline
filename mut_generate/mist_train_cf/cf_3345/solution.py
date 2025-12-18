"""
QUESTION:
Write a function `convert_lists` that takes two lists, `list1` and `list2`, as input and returns a new list containing concatenated items from `list1` and `list2` without using the 'if' statement, built-in functions, or methods. The function should only consider strings from `list1` and integers from `list2`. The result should only include concatenated items where the string from `list1` is greater than 10 when treated as an integer.
"""

def convert_lists(list1, list2):
    """
    This function takes two lists as input, concatenates their items, 
    and returns a new list. It only considers strings from list1 and 
    integers from list2. The result only includes concatenated items 
    where the string from list1 is greater than 10 when treated as an integer.

    Args:
        list1 (list): The list containing strings to be concatenated.
        list2 (list): The list containing integers to be concatenated.

    Returns:
        list: A new list containing concatenated items.
    """
    result_list = [str(list1[i]) + str(list2[j]) for i in range(len(list1)) for j in range(len(list2)) if isinstance(list1[i], str) and isinstance(list2[j], int) and int(list1[i]) > 10]
    return result_list