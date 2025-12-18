"""
QUESTION:
Implement the function `find_longest_even_words(words: List[str]) -> List[str]` to find the word(s) with the longest length that contains an even number of characters in a given list of words. The list `words` contains 1 to 1000 strings, each consisting of only lowercase letters and having a length between 1 and 100 (inclusive). The function should return a list of strings containing the word(s) with the longest length that contains an even number of characters.
"""

from typing import List

def find_longest_even_words(words: List[str]) -> List[str]:
    max_length = 0
    result = []
    
    for word in words:
        if len(word) % 2 == 0:
            if len(word) > max_length:
                max_length = len(word)
                result = [word]
            elif len(word) == max_length:
                result.append(word)
    
    return result