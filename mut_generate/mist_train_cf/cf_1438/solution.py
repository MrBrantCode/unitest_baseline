"""
QUESTION:
Implement a function `capitalize_names` that takes a list of strings and returns a modified list where each string has its first letter capitalized and all other letters converted to lowercase. The function should handle strings with mixed cases, special characters, digits, spaces, and strings with multiple words separated by spaces. It should also handle strings with non-alphabetic characters in the middle of the word.
"""

from typing import List

def capitalize_names(names: List[str]) -> List[str]:
    modified_names = []
    for name in names:
        words = name.split(" ")
        capitalized_words = []
        for word in words:
            capitalized_word = word.lower().capitalize()
            capitalized_words.append(capitalized_word)
        modified_name = " ".join(capitalized_words)
        modified_names.append(modified_name)
    return modified_names