"""
QUESTION:
Compare two input strings without using built-in string comparison functions or libraries. Implement a function named `compare_strings` that takes two string parameters and returns a boolean value indicating whether they are identical. The function must compare the strings character by character and return False as soon as a mismatch is found, or True if all characters match.
"""

def compare_strings(s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True