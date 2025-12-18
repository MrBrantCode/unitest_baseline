"""
QUESTION:
Create a function called `check_string` that takes a string `s` as an argument and checks if it contains only unique, lowercase alphabets in lexicographical order. The function should return a boolean value indicating whether the string meets these conditions. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string, which will be at most 1000 characters.
"""

def check_string(s):
    if len(s) != len(set(s)):
        return False

    for char in s:
        if not char.islower():
            return False

    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            return False

    return True