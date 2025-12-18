"""
QUESTION:
Implement a function `word_pattern` that takes in two parameters: `pattern` and `str`. The `pattern` is a string of unique lowercase alphabetical characters without spaces, and `str` is a string of space-separated words. The function should return `True` if the pattern matches the input string and `False` otherwise, where a match is defined as each character in the pattern being mapped to a word in the string consistently.
"""

def word_pattern(pattern: str, str: str) -> bool:
    words = str.split(" ")
    if len(pattern) != len(words):
        return False
    
    pattern_map = {}
    word_map = {}
    
    for char, word in zip(pattern, words):
        if char not in pattern_map:
            pattern_map[char] = word
        else:
            if pattern_map[char] != word:
                return False
            
        if word not in word_map:
            word_map[word] = char
        else:
            if word_map[word] != char:
                return False
    
    return True