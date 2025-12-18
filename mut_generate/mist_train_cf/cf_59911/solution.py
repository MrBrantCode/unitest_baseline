"""
QUESTION:
Create a function named `remove_repeats` that removes all repeated elements from a list while maintaining the original order of the remaining elements. Do not use Python-specific functions like OrderedDict. Consider multiple None or multiple NULL values as repeated elements. The function should work with any list of elements.

Restrictions: Do not use Python-specific functions like OrderedDict.
"""

def remove_repeats(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list