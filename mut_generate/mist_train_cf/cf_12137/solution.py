"""
QUESTION:
Write a function `are_anagrams(s1, s2)` that checks if two input strings `s1` and `s2` are anagrams, considering both uppercase and lowercase letters. The function should ignore any whitespace in the input strings and return `True` if the strings are anagrams, and `False` otherwise.
"""

def are_anagrams(s1, s2):
    # Convert both strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()

    # Remove whitespace from both strings
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    # Sort both strings alphabetically
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    # Check if the sorted strings are equal
    return sorted_s1 == sorted_s2