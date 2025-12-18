"""
QUESTION:
Create a function `complex_match(lst1, lst2, unique_chars=True, ignore_nums=True)` that accepts two lists of strings, `lst1` and `lst2`, and returns the list with the lowest total character count, considering only alphanumeric characters and disregarding spaces. If both lists hold the same count, return `lst1`. The function should also consider the following parameters: 
- `unique_chars`: a boolean parameter (default to True) that when set to True, only consider unique characters in each string.
- `ignore_nums`: a boolean parameter (default to True) that when set True, numbers in strings are disregarded when counting characters.
The original order of elements in the lists should be preserved.
"""

def complex_match(lst1, lst2, unique_chars=True, ignore_nums=True):
    from collections import Counter
    from string import ascii_letters

    def count_characters(lst):
        count = Counter()
        for word in lst:
            if ignore_nums:
                word = ''.join(c for c in word if c in ascii_letters or c.isspace())
            if unique_chars:
                count.update(set(word.replace(" ", "")))
            else:
                count.update(word.replace(" ", ""))
        return sum(count.values())

    return lst1 if count_characters(lst1) <= count_characters(lst2) else lst2