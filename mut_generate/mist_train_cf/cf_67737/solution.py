"""
QUESTION:
Create a function `custom_string_list` that takes a list of strings and an optional boolean `reverse` parameter (defaulting to False) as input. The function should return a new list containing only the input strings that have at least one vowel and no special characters, sorted first by length in ascending order (or descending if `reverse` is True) and then alphabetically for strings of the same length. The function should ignore capitalization and numeric characters when sorting.
"""

import re

def custom_string_list(lst, reverse=False):
    def has_special_char(s):
        return bool(re.search('[^A-Za-z]', s))

    def has_vowel(s):
        return bool(re.search('[aeiou]', s.lower()))

    new_list = [x for x in lst if x and not has_special_char(x) and has_vowel(x)]

    new_list.sort(key=lambda x: (len(x), x.lower()), reverse=reverse)

    return new_list