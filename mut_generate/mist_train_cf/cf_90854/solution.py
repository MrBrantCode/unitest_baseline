"""
QUESTION:
Write a function `are_anagrams(str1, str2)` that checks if two input strings are anagrams, ignoring case and non-alphanumeric characters. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the total number of alphanumeric characters in the input strings.
"""

def are_anagrams(str1, str2):
    # Convert strings to lowercase and remove non-alphanumeric characters
    str1 = ''.join(c.lower() for c in str1 if c.isalnum())
    str2 = ''.join(c.lower() for c in str2 if c.isalnum())

    # Sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2