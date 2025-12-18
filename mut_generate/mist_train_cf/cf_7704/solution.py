"""
QUESTION:
Implement the function `find_longest_even_words(words: List[str]) -> List[str]`, which takes a list of strings representing words and returns a list of strings containing the word(s) with the longest length that contains an even number of characters. Each word consists of only lowercase letters and has a length between 1 and 100 (inclusive). The order of the words in the output list does not matter.
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