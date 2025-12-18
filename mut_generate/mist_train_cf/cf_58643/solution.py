"""
QUESTION:
Create a function `duplicate_string_filter` that takes in three parameters: a string `s`, a boolean `include_nums` (defaulting to False), and an integer `min_word_length` (defaulting to 0). The function should return a duplicate of the input string `s`, excluding any embedded grammar symbols, punctuation, or whitespaces. The function should include numbers in the resulting string if `include_nums` is True. Additionally, it should only include words in the resulting string that have a length greater than or equal to `min_word_length`.
"""

import string

def duplicate_string_filter(s, include_nums=False, min_word_length=0):
    valid_chars = string.ascii_letters  
    if include_nums:
        valid_chars += string.digits
    new_str = ''
    s_split = s.split()
    for word in s_split:
        if len(word) >= min_word_length:
            temp_str = ''
            for char in word:
                if char in valid_chars:
                    temp_str += char
            new_str += temp_str
    return new_str*2