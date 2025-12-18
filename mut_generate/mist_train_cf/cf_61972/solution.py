"""
QUESTION:
Write a function total_match_case_insensitive(lst1, lst2, unique_chars=True) that compares two lists of strings and returns the list with the lower total character count in the strings (ignoring spaces and case differences, and non-alphabetic characters). If both lists have the same number of characters, return the first list. The unique_chars parameter, which defaults to True, determines whether to count only unique characters in each string. The function must preserve the original order of elements in the list.
"""

import re

def total_match_case_insensitive(lst1, lst2, unique_chars=True):
    def count_chars(lst, unique_chars):
        count = 0
        for word in lst:
            word = re.sub(r'\W|\d', '', word.lower())
            if unique_chars:
                word = ''.join(set(word))
            count += len(word)
        return count

    chars1 = count_chars(lst1, unique_chars)
    chars2 = count_chars(lst2, unique_chars)
    if chars1 <= chars2:
        return lst1
    else:
        return lst2