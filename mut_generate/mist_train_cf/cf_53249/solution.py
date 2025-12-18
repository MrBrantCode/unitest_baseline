"""
QUESTION:
Design a function named `evaluate_string_list` that takes a list of strings as input and returns the total sum of ASCII values calculated for each string. If a string contains a semicolon or double colon, calculate the sum of ASCII values for each substring after splitting the string. If neither semicolon nor double colon exists, calculate the sum of ASCII values for uppercase alphabetic characters at even indices (0-based, i.e., 'A' is at index 0, 'B' is at index 1, ..., 'Z' is at index 25).
"""

def evaluate_string_list(sl):
    ascii_sum = 0
    for s in sl:
        if ';' in s or '::' in s:
            if ';' in s:
                res_list = s.split(';')
            elif '::' in s:
                res_list = s.split('::')
            for item in res_list:
                ascii_sum += sum(ord(c) for c in item)
        else:
            ascii_sum += sum(ord(c) for i, c in enumerate(s) if i % 2 == 0 and c.isupper())
    return ascii_sum