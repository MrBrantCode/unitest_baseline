"""
QUESTION:
Write a function named `count_unique_words` that takes a string as input and returns the count of unique words in the string, ignoring case, punctuation, and special characters. The function should handle plural and possessive forms of words as the same word, and consider contractions as the same word as their non-contracted forms. The function must be implemented manually without using any built-in functions or libraries for string manipulation or word counting.
"""

def count_unique_words(string):
    string = string.strip()
    unique_words = set()
    current_word = ''
    is_forming_word = False

    for char in string:
        if char.isalpha() or char == "'":
            current_word += char
            is_forming_word = True
        else:
            if is_forming_word:
                unique_words.add(current_word.lower())
                current_word = ''
                is_forming_word = False

    if is_forming_word:
        unique_words.add(current_word.lower())

    return len(unique_words)