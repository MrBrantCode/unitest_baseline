"""
QUESTION:
Write a function `get_max_strings_with_digits_and_special_chars` that takes a list of strings as input and returns the two strings with the maximum length that contain at least one digit and one special character from the set: @, !, #, $, %, ^, &, *, (, ).
"""

def get_max_strings_with_digits_and_special_chars(str_list):
    max_str_1 = ""
    max_str_2 = ""
    max_len_1 = 0
    max_len_2 = 0
    for s in str_list:
        # check if string contains at least one digit and one special character
        if any(c.isdigit() for c in s) and any(c in "@!#$%^&*()" for c in s):
            s_len = len(s)
            # if length of current string is greater than max_str_1, update max_str_1 and max_len_1
            if s_len > max_len_1:
                max_str_2 = max_str_1
                max_len_2 = max_len_1
                max_str_1 = s
                max_len_1 = s_len
            # if length of current string is greater than max_str_2 but less than max_str_1, update max_str_2 and max_len_2
            elif s_len > max_len_2 and s_len <= max_len_1:
                max_str_2 = s
                max_len_2 = s_len
    return [max_str_1, max_str_2]