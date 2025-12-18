"""
QUESTION:
Write a function named `check_second_letter` that accepts an array of words and returns `True` if any word contains the vowel `e` in its second letter position, and `False` otherwise. The function should return immediately after finding a word with `e` as the second letter.
"""

def check_second_letter(words):
    for word in words:
        if len(word) >= 2 and word[1] == 'e':
            return True
    return False