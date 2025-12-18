"""
QUESTION:
Write a function `remove_vowels_recursive` that takes a string `s` as input and returns a new string with all vowels removed. The function should have a time complexity of O(n), where n is the length of the input string, and use constant space complexity. It should handle both uppercase and lowercase vowels, and any occurrence of a vowel should be removed regardless of its position in the word. The function should be implemented recursively.
"""

def remove_vowels_recursive(s):
    if len(s) == 0:
        return ""
    elif s[0].lower() in "aeiou":
        return remove_vowels_recursive(s[1:])
    else:
        return s[0] + remove_vowels_recursive(s[1:])