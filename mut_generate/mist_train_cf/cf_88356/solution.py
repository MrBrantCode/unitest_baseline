"""
QUESTION:
Write a function `count_distinct_words` that takes a string as input and returns the number of distinct alphabetic words it contains, ignoring special characters, numbers, and case sensitivity. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in Python functions or libraries for string manipulation or counting.
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