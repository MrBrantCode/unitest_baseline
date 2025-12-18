"""
QUESTION:
Implement a function `test_char` that takes a single character as input and returns `True` if the character is an uppercase letter, or its Unicode point value if the character is a non-alphanumeric symbol. The function should return `False` for all other cases, including lowercase letters, numbers, and alphanumeric characters.
"""

def test_char(char):
    if char.isupper():
        return True
    if not char.isalnum():
        return ord(char)
    return False