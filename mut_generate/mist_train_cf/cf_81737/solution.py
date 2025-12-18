"""
QUESTION:
Write a function `advanced_string_manipulation` that takes four parameters: `s`, `target`, `delimiter_set`, `r_flag`, and `c_flag`. The function should split the input string `s` into words using any number of delimiters from the `delimiter_set`, exclude words that match the `target` string (case-sensitive if `c_flag` is `True`), and reverse the order of characters in the remaining words if `r_flag` is `True`. Return the resulting list of words.
"""

import re

def advanced_string_manipulation(s, target, delimiter_set, r_flag, c_flag):
    # Replace all delimiters in the string with a space, making it easier to split later
    s_modified = s.translate(str.maketrans({key: ' ' for key in delimiter_set}))

    # Separate the string into a list of words.
    words_list = re.findall(r"[\w']+", s_modified)

    # Handle the 'target' word match case-sensitivity
    if not c_flag:
        words_list = [i for i in words_list if i.lower() != target.lower()]
    else:
        words_list = [i for i in words_list if i != target]

    # If 'r_flag' is True, reverse the order of each word in the list
    if r_flag:
        words_list = [i[::-1] for i in words_list]

    return words_list