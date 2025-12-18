"""
QUESTION:
Design a function `is_palindrome(s)` that determines whether a given string `s` is a palindrome, ignoring non-alphanumeric characters and case. The function must have a time complexity of O(n), where n is the length of `s`, and cannot use built-in string manipulation functions.
"""

def is_palindrome(s):
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