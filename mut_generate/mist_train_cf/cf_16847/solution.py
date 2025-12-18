"""
QUESTION:
Implement a function named `is_anagram` that determines if two input strings, s1 and s2, are anagrams of each other. The function should ignore case sensitivity, remove non-alphabetic characters, and compare the sorted alphabetic characters. The time complexity of the solution should be O(nlogn), where n is the length of the longer string between s1 and s2, and no built-in functions or libraries for sorting or comparing strings are allowed.
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
    return s1 == s2