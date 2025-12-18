"""
QUESTION:
Create a function called `long_words_with_case` that takes a string as input and returns a list of words that meet the following conditions:
- The word is longer than 10 characters
- The word contains at least one uppercase letter
- The word contains at least one lowercase letter
"""

def long_words_with_case(string):
    words = string.split()
    result = []

    for word in words:
        if len(word) > 10 and any(char.islower() for char in word) and any(char.isupper() for char in word):
            result.append(word)

    return result