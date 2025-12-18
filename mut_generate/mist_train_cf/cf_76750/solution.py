"""
QUESTION:
Develop a function named `check_string_order` that takes two number strings (`str_num1` and `str_num2`) and a boolean parameter (`cond`). It checks if all digits of `str_num2` are in the same order in `str_num1`. If `cond` is `True`, the digits must be consecutively found in `str_num1`. Return `True` if the condition is met, and `False` otherwise.
"""

def check_string_order(str_num1, str_num2, cond):
    if cond:    # if the boolean is True
        return str_num2 in str_num1
    else:   # if the boolean is False
        j = 0
        for i in range(len(str_num1)):
            if str_num1[i] == str_num2[j]:
                j += 1
                if j == len(str_num2):
                    return True
        return False