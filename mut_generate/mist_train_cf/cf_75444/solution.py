"""
QUESTION:
Write a function `max_run_uppercase(s)` that takes a string `s` as input and returns a tuple containing the starting and ending index of the maximum run of consecutive uppercase characters in `s`. If there are multiple runs of the same length, return the indices of the first one.
"""

def max_run_uppercase(s):
    max_len = 0
    max_start = max_end = 0
    current_len = 0
    current_start = current_end = 0

    for i in range(len(s)):
        if s[i].isupper():
            if current_len == 0:
                current_start = i
            current_len += 1
            current_end = i

            if current_len > max_len:
                max_len = current_len
                max_start = current_start
                max_end = current_end
        else:
            current_len = 0

    return max_start, max_end