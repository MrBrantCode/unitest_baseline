"""
QUESTION:
Create a function named `check_string` that takes a string `s` as input and checks if it contains only alphabetic characters from the English language and a balanced set of parentheses. The function should return `True` if the string is valid, "Unbalanced parentheses" if the string contains unbalanced parentheses, and "Contains non-alphabetic characters" if the string contains non-alphabetic characters. Note that the function should handle edge cases where the string may contain multiple parentheses and non-alphabetic characters.
"""

def check_string(s):
    check_string = set(s)
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if check_string.issubset(alphabet.union(set('()'))):
        if s.count('(') == s.count(')'):
            return True
        else:
            return "Unbalanced parentheses"
    else:
        return "Contains non-alphabetic characters"