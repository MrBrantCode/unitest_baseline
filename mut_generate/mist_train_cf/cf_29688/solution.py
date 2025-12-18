"""
QUESTION:
Create a function `filter_words` that takes a list of words and the specified minimum and maximum lengths as input. The function should return a new list containing only the words that meet all the following conditions:
- The length of the word is greater than or equal to the minimum length and less than or equal to the maximum length.
- The word contains at least one special character.
- The word contains at least one lowercase letter.
- The word contains at least one uppercase letter.

Function Signature: `def filter_words(words: List[str], minlength: int, maxlength: int) -> List[str]`
"""

import re
from typing import List

def filter_words(words: List[str], minlength: int, maxlength: int) -> List[str]:
    filtered_words = []
    specials = re.compile(r'[^A-Za-z0-9\s]')
    lowers = re.compile(r'[a-z]')
    uppers = re.compile(r'[A-Z]')

    for word in words:
        word = word.strip()
        if (minlength <= len(word) <= maxlength 
            and specials.search(word) is not None 
            and lowers.search(word) is not None 
            and uppers.search(word) is not None):
            filtered_words.append(word)

    return filtered_words