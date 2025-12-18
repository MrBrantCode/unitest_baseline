"""
QUESTION:
Write a function named `filter_strings` that takes a list of strings as input, filters out strings with a length less than 2 characters or not in uppercase, and returns the filtered list in descending order of string length. In case of strings with the same length, sort them in lexicographical order.
"""

def filter_strings(lst):
    filtered_lst = []
    for string in lst:
        if len(string) >= 2 and string.isupper():
            filtered_lst.append(string)
    filtered_lst.sort(key=lambda x: (-len(x), x))
    return filtered_lst