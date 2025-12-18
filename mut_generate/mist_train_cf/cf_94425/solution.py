"""
QUESTION:
Write a function named `is_anagram` that takes two string parameters `s1` and `s2`. The function should return `True` if `s1` is an anagram of `s2` and `False` otherwise, ignoring case sensitivity and non-alphabetic characters. The function must implement the sorting and comparison logic itself without using any built-in functions or libraries for sorting or comparing strings. The time complexity of the solution should be O(nlogn), where n is the length of the longer string between `s1` and `s2`.
"""

def is_anagram(s1, s2):
    # Step 1: Convert to lowercase
    s1 = s1.lower()
    s2 = s2.lower()

    # Step 2: Remove non-alphabetic characters
    s1 = ''.join(c for c in s1 if c.isalpha())
    s2 = ''.join(c for c in s2 if c.isalpha())

    # Step 3: Sort characters
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    # Step 4: Compare sorted strings
    if s1 == s2:
        return True
    else:
        return False