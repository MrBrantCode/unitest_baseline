"""
QUESTION:
Create a function `remove_duplicates` that takes a list of elements as input, removes duplicates while maintaining the original order of elements, and returns the updated list. The function must have a time complexity of O(n), where n is the length of the input list, and cannot use any built-in functions or additional data structures beyond basic list operations. The function should handle lists containing integers, floats, and strings, remove duplicates case-insensitively for strings, and be able to handle lists with up to 100,000 elements, including duplicates appearing consecutively and empty lists.
"""

def remove_duplicates(lst):
    updated_lst = []
    for i in lst:
        if isinstance(i, str):
            i = i.lower()
        if i not in updated_lst:
            updated_lst.append(i)
    return updated_lst