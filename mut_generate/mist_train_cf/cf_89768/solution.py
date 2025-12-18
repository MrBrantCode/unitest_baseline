"""
QUESTION:
Write a function `print_reverse_vowels` that takes a string `s` and an index `i` as parameters, prints each vowel in the string individually in reverse order, and has a time complexity of O(n) and a space complexity of O(1). The function should not use any built-in string manipulation functions or loops.
"""

def print_reverse_vowels(s, i):
    if i < 0 or i >= len(s):
        return
    
    if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
        print(s[i])
    
    print_reverse_vowels(s, i-1)