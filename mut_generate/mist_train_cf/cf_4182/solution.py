"""
QUESTION:
Write a function called `count_distinct_words` that takes a string as input and returns the number of distinct words in the string. The function should ignore non-alphabetic characters and be case-insensitive, treating uppercase and lowercase letters as the same. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string manipulation or counting functions/libraries beyond basic operations.
"""

def count_distinct_words(string):
    words = set()
    current_word = ""
    lowercase_string = string.lower()
    
    for c in lowercase_string:
        if c.isalpha():
            current_word += c
        elif current_word:
            words.add(current_word)
            current_word = ""

    if current_word:
        words.add(current_word)

    return len(words)