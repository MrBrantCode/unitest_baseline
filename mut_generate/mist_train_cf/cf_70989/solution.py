"""
QUESTION:
Write a function `concat_two_lists(list1, list2)` that accepts two lists of strings as inputs and returns a new list containing the concatenated strings. The function should concatenate corresponding elements from each list, considering missing elements in the shorter list as empty strings.
"""

from itertools import zip_longest

def concatenate_two_lists(list1, list2):
    return [''.join((str(a or ''), str(b or ''))) for a, b in zip_longest(list1, list2)]