"""
QUESTION:
Implement a function named `create_frequency_chart` that takes a string `text` as input and returns a dictionary containing the frequency of each unique word in the text, without using built-in string or dictionary functions like `split()` or `Counter`. The function should be case-insensitive, count words with apostrophes as single words, and have a time complexity of O(n), where n is the length of the input string `text`.
"""

def create_frequency_chart(text):
    frequency_chart = {}

    # Convert text to lowercase to count words case-insensitively
    text = text.lower()

    word = ""
    for char in text:
        # Check if the character is a letter or an apostrophe
        if char.isalpha() or char == "'":
            word += char
        # Check if the word is not empty and we have reached a non-letter character
        elif word:
            if word in frequency_chart:
                frequency_chart[word] += 1
            else:
                frequency_chart[word] = 1
            word = ""

    # Check if there is a word at the end of the text
    if word:
        if word in frequency_chart:
            frequency_chart[word] += 1
        else:
            frequency_chart[word] = 1

    return frequency_chart