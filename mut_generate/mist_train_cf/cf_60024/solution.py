"""
QUESTION:
Create a function called `total_match(lst1, lst2, unique_chars=True)` that takes two lists of string values and returns the list with the lesser total character count amongst all the strings. The function should ignore all spaces and maintain the initial order of elements in the list. If a tie arises between both lists, it should favour the first list. The `unique_chars` parameter determines whether to only incorporate unique characters while counting, defaulting to `True`.
"""

def total_match(lst1, lst2, unique_chars=True):
    def total_chars(lst):
        str_concat = ''.join(lst).replace(' ', '')
        return len(set(str_concat)) if unique_chars else len(str_concat)

    return lst1 if total_chars(lst1) <= total_chars(lst2) else lst2