"""
QUESTION:
Write a function `find_anagram_in_dictionary(input_str, dictionary_words)` that takes a string `input_str` and a list of dictionary words `dictionary_words` as input, and returns the anagram of the `input_str` found in the `dictionary_words` list. If no anagram is found, the function should return an empty string.
"""

from typing import List

def find_anagram_in_dictionary(input_str: str, dictionary_words: List[str]) -> str:
    sorted_input_str = sorted(input_str)
    
    for word in dictionary_words:
        if sorted(word) == sorted_input_str:
            return word

    return ""