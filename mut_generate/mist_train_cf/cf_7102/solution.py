"""
QUESTION:
Create a function `print_reverse_vowels` that takes a string `s` and an index `i` as parameters. The function should print each vowel in the string `s` individually in reverse order without using any built-in string manipulation functions or loops. The time complexity should be O(n) and the space complexity should be O(1).
"""

def print_reverse_vowels(s, i):
    if i < 0 or i >= len(s):
        return
    
    if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
        print(s[i])
    
    print_reverse_vowels(s, i-1)