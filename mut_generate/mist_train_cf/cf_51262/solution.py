"""
QUESTION:
Create a function called `priority_mapper` that takes a string `s` and a list `p` as input. The function should remove any non-numeric characters from `s` and any duplicate elements from `p` while preserving order. If `p` is empty, return the reversed list of numeric characters from `s` if the percentage of non-numeric characters is less than or equal to 50%. Otherwise, print an error message and return an empty list. If `p` is not empty, return the list of characters from `p` that are present in `s`, in the order of their first occurrence in `p`.
"""

def priority_mapper(s, p):
    s = [char for char in s if char.isdigit()]
    error_margin = len(s) / 2

    if p == []:
        if len(s) / (len(s) + len([char for char in s if not char.isdigit()])) > 0.5:
            print("Error: More than 50% of the characters are unrecognizable.")            
            return []
        else:
            return s[::-1]
    else:
        p = list(dict.fromkeys(p))
        mapped_chars = [char for char in p if char in s]
        return mapped_chars