"""
QUESTION:
Create a function `check_valid_words` that takes a list of strings as input and returns `True` if all unique words in the list are valid English words, and `False` otherwise. The function should ignore case sensitivity and consider each word only once, even if it appears multiple times in the list. The set of valid English words should be predefined within the function.
"""

def check_valid_words(words):
    validWords = {"hello", "world"}  # Replace with a set of valid English words

    uniqueWords = set()

    for word in words:
        lowercaseWord = word.lower()
        if lowercaseWord not in uniqueWords:
            if lowercaseWord in validWords:
                uniqueWords.add(lowercaseWord)

    return len(uniqueWords) == len(validWords)