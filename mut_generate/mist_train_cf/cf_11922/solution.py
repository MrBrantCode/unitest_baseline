"""
QUESTION:
Design a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome or not, ignoring non-alphanumeric characters and considering the comparison case-insensitive. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions.
"""

def entance(s):
    i = 0
    j = len(s) - 1

    while i < j:
        # Increment i if the current character is non-alphanumeric
        while i < j and not s[i].isalnum():
            i += 1
        # Decrement j if the current character is non-alphanumeric
        while i < j and not s[j].isalnum():
            j -= 1

        # Compare the characters at i and j (ignoring case)
        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True