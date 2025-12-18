"""
QUESTION:
Write a function `max_uppercase_run` that takes a string `s` as input and returns the starting and ending indices of the maximum run of consecutive uppercase characters in the string. The function should ignore special characters and numbers when determining the run. If there are multiple runs of the same length, return the indices of the first one.
"""

def max_uppercase_run(s):
    max_len = 0
    max_start = 0
    max_end = 0

    current_len = 0
    start = 0
    for i in range(len(s)):
        if s[i].isupper():
            if current_len == 0:
                start = i
            current_len = current_len + 1
            if current_len > max_len:
                max_len = current_len
                max_start = start
                max_end = i
        else:
            current_len = 0   

    return max_start, max_end