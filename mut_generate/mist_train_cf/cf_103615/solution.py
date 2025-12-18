"""
QUESTION:
Write a function `count_characters(s1, s2)` that takes two strings `s1` and `s2` as input and returns the total count of occurrences of all characters in `s2` present in `s1`. The function should consider the following constraints:

* The function is case-sensitive and should treat 'o' and 'O' as different characters.
* The characters in `s2` can be repeated, and each occurrence should be counted separately.
* `s1` and `s2` can contain any printable ASCII characters, including letters, digits, symbols, and whitespace.

The function should return the total count of occurrences of all characters in `s2` present in `s1`.
"""

def count_characters(s1, s2):
    count = 0
    for char in s2:
        count += s1.count(char)
    return count