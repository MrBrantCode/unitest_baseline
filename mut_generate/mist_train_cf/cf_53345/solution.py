"""
QUESTION:
Design a function named `is_anagram` that verifies whether a given word is an anagram of its reversed form or not. The function should accept a string input, validate if it contains only alphanumeric characters, and return a boolean value indicating whether the input string is an anagram of its reverse. If the input is not a string, the function should return an error message. Implement the function with optimal time complexity, ideally O(n), where 'n' is the length of the input string.
"""

def is_anagram(word):
    if not isinstance(word, str):
        return "Invalid input! Please enter a string."
    
    word = ''.join(e for e in word if e.isalnum()).lower()
    return word == word[::-1]