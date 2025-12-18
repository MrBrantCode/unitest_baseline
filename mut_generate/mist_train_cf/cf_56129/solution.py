"""
QUESTION:
Write a function `count_sub_sequences` that takes a string as input and returns the total number of unique, uninterrupted sub-sequences within the string. The function should be able to handle strings containing alphanumeric characters, punctuation, and whitespace, and should only count each repeating sequence once.
"""

def count_sub_sequences(string):
    substrings = set()

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substrings.add(string[i:j])

    return len(substrings) - 1