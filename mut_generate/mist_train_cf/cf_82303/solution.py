"""
QUESTION:
Create a function `punctuation_check(text)` that validates whether a given text string contains between 2 and 10 punctuation marks. The function should only count punctuation marks commonly used in English texts and exclude non-punctuation special characters. The function should return `True` if the text string contains between 2 and 10 punctuation marks, and `False` otherwise.
"""

import string

def punctuation_check(text):
    punctuation_marks = ".,!?;:-()[]{}'\""
    count = 0
    for character in text:
        if character in punctuation_marks:
            count += 1
    return 2 <= count <= 10