"""
QUESTION:
Create a function `long_words_with_case` that takes a string as input. The function should return a list of words from the string that are longer than 10 characters and contain at least one uppercase letter and one lowercase letter.
"""

def long_words_with_case(string):
    words = string.split()  
    result = []

    for word in words:
        if len(word) > 10 and any(char.islower() for char in word) and any(char.isupper() for char in word):
            result.append(word)

    return result