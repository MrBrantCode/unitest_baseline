"""
QUESTION:
Create a function named `filter_strings` that takes a list of strings and an integer `n` as input, and returns a new list of strings that contain both uppercase and lowercase letters and have a length greater than or equal to `n`.
"""

def filter_strings(lst, n):
    filtered_lst = []
    for string in lst:
        if any(char.islower() for char in string) and any(char.isupper() for char in string) and len(string) >= n:
            filtered_lst.append(string)
    return filtered_lst