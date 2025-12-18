"""
QUESTION:
Design a function named `find_substring_indices` that determines the starting indices of all occurrences of a given substring in a given string. The function should take three parameters: the main string, the substring to find, and a boolean flag indicating whether the search should be case sensitive. The function should return the starting indices of all occurrences of the substring.
"""

def find_substring_indices(main_string, substring, case_sensitive):
    main_string = main_string if case_sensitive else main_string.lower()
    substring = substring if case_sensitive else substring.lower()

    start = 0
    while True:
        start = main_string.find(substring, start)
        if start == -1: return
        yield start
        start += 1