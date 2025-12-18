"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of elements as input and returns the list with duplicate elements removed while maintaining the original order. The function should have a time complexity of O(n), where n is the length of the input list, and should not use any built-in functions or methods that directly remove duplicates from a list, or any additional data structures. The function should be able to handle lists with up to 100,000 elements, containing integers, floats, and strings, and should remove duplicates case-insensitively for strings.
"""

def remove_duplicates(lst):
    result = []
    for i in lst:
        if isinstance(i, str):
            i_lower = i.lower()
            if i_lower not in (str(x).lower() if isinstance(x, str) else x for x in result):
                result.append(i)
        else:
            if i not in result:
                result.append(i)
    return result