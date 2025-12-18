"""
QUESTION:
Create a function `substitute_str(str1, str2, sentence)` that takes three parameters: the original string `str1`, the replacement string `str2`, and the input `sentence`. Replace the first occurrence of `str1` in `sentence` with `str2` and return the modified sentence. The function should only replace the first occurrence, leaving any subsequent occurrences of `str1` unchanged.
"""

def substitute_str(str1, str2, sentence):
    return sentence.replace(str1, str2, 1)