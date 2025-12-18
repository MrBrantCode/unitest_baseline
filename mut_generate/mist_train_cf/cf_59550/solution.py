"""
QUESTION:
Write a function `distinct_substrings(s1, s2)` that calculates the total number of distinct substrings in string `s1` that contain all the characters in string `s2` at least once, with the condition that each character in `s2` is unique and the function should be case-sensitive. The function should return the count of such substrings. The function should handle cases where `s1` is shorter than `s2` or either of the strings is empty.
"""

def distinct_substrings(s1, s2):
    if not s2 or not s1 or len(s1) < len(s2):
        return 0

    s2_chars = set(s2)
    counted_substrings = set()
    left = 0
    current_chars = set()

    for right in range(len(s1)):
        current_chars.add(s1[right])

        while current_chars.issuperset(s2_chars):
            counted_substrings.add(s1[left:right+1])
            current_chars.remove(s1[left])
            left += 1

    return len(counted_substrings)