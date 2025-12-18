"""
QUESTION:
Write a function called `palindrome_anagram(s)` that determines whether the input string `s` can be rearranged into a palindrome. The function should ignore spaces and be case-insensitive. The input string is expected to contain alphanumeric characters.
"""

def can_form_palindrome(s):
    s = s.replace(' ','').lower()
    dictionary = {}
    odd_valued_keys = []
    for i in s:
        if i not in dictionary:
            dictionary[i] = 1
        elif i in dictionary:
            dictionary[i] += 1
    
    for key, value in dictionary.items():
        if value%2 != 0:
            odd_valued_keys.append(key)

    if len(odd_valued_keys) > 1:
        return False
    return True