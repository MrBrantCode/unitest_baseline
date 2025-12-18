"""
QUESTION:
Create a function named `are_anagrams` that takes two string parameters, `s1` and `s2`. The function should check if `s1` and `s2` are anagrams of each other, disregarding case and whitespace. The function should return a boolean value indicating whether the strings are anagrams or not.
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