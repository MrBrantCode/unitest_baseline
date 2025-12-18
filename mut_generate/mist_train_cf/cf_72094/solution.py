"""
QUESTION:
Write a function `total_match(lst1, lst2, unique_chars=True)` that accepts two lists of strings and returns the list with the lower total character count in the strings (ignoring spaces and numbers) while preserving the original order of elements in the list. If both lists have the same number of characters, return the first list. When `unique_chars` is set to `True`, only count unique characters in each string.
"""

def total_match(lst1, lst2, unique_chars=True):
    def char_count(lst, unique_chars):
        count = 0
        for s in lst:
            if unique_chars:
                count += len(set(s)-set("0123456789 "))-1 if len(s) > 0 else 0
            else:
                count += sum(x not in "0123456789 " for x in s)
        return count

    count1 = char_count(lst1, unique_chars)
    count2 = char_count(lst2, unique_chars)

    return lst1 if count1 <= count2 else lst2