"""
QUESTION:
Write a function called `extract_content` that takes a string `s`, a start character `start_char`, and an end character `end_char` as input. The function should return the substring of `s` that starts after the first occurrence of `start_char` and ends before the first occurrence of `end_char` that follows the `start_char`. The function should return an empty string if `start_char` or `end_char` is not found in `s`, or if `end_char` comes before `start_char`.
"""

def extract_content(s, start_char, end_char):
    start = s.find(start_char) + 1
    if start == 0:
        return ""
    end = s.find(end_char, start)
    if end == -1:
        return ""
    return s[start:end]