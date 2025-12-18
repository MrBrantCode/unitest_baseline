"""
QUESTION:
Create a function named `is_anagram` that takes two strings as arguments. The function should return `True` if the two strings are anagrams (same letters arranged differently), and `False` otherwise. 

The function should ignore case, whitespace, and non-alphabetic characters. If either string is empty or contains only whitespace characters after removing leading/trailing whitespace, the function should return `False`.
"""

def is_anagram(s, t):
    # Remove leading and trailing whitespace
    s = s.strip()
    t = t.strip()

    # Convert both strings to lowercase
    s = s.lower()
    t = t.lower()

    # Remove non-alphabetic characters
    s = ''.join(ch for ch in s if ch.isalpha())
    t = ''.join(ch for ch in t if ch.isalpha())

    # Check for empty strings or strings with only whitespace
    if not s or not t:
        return False

    # Sort both strings alphabetically
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    # Compare the sorted strings
    if sorted_s == sorted_t:
        return True
    else:
        return False