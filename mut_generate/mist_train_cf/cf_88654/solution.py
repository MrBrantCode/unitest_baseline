"""
QUESTION:
Write a function `string_formatter(s)` that takes a string `s` as input, splits it into a list of words, removes any duplicate words, and returns the list of unique words in alphabetical order. The function should ignore any punctuation marks and consider words with different capitalizations as the same word. Implement the function using a single pass over the input string and do not use any built-in functions or libraries for sorting or duplicate removal. The time complexity of the solution should be O(n log n) or better.
"""

def string_formatter(s):
    words = []
    word = ''
    for char in s:
        if char.isalpha():
            word += char.lower()
        elif word:
            words.append(word)
            word = ''
    if word:
        words.append(word)

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    sorted_words = sorted(unique_words)
    return sorted_words