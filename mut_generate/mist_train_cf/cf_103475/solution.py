"""
QUESTION:
Create a function `concatenate_lists` that takes two lists `list1` and `list2` as parameters. The function should combine the elements of `list1` and `list2` into a new list without using built-in Python list concatenation functions or methods. If either `list1` or `list2` is empty, the function should return a corresponding message, and if both are empty, it should return a message indicating both are empty.
"""

def concatenate_lists(list1, list2):
    if not list1 and not list2:
        return "Both lists are empty."
    elif not list1:
        return "List1 is empty."
    elif not list2:
        return "List2 is empty."
    else:
        result = []
        for item in list1:
            result.append(item)
        for item in list2:
            result.append(item)
        return result