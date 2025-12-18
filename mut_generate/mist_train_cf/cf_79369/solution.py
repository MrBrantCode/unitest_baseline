"""
QUESTION:
Design a function called `evaluate_string(s)` that takes a string `s` as input and returns either a list of phrases or an integer. The string is split into phrases if it contains a semicolon ';' or double colon '::'. If neither exists, the function returns the sum of the indices of upper-case alphabetic characters with even indices in the alphabet (where 'A' has an index of 0).
"""

def evaluate_string(s):
    if ';' in s:
        return s.split(';')
    elif '::' in s:
        return s.split('::')
    else:
        upper_case_sum = 0
        for char in s:
            if char.isupper():
                index = ord(char) - ord('A')
                if index % 2 == 0:
                    upper_case_sum += index
        return upper_case_sum