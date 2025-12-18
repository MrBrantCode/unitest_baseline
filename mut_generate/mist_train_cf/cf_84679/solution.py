"""
QUESTION:
Create a function named `word_array_filter` that takes a string `s` and a target word `target` as parameters. The string `s` contains words separated by spaces, commas, or both. The function should return an array of words in the original sequence, excluding all instances of the `target` word.
"""

def word_array_filter(s, target):
    # replace commas followed by a space with a space
    s = s.replace(', ', ' ')
    # split the string into words based on space
    words = s.split(' ')
    # filter words and exclude the target
    filtered_words = [word for word in words if word != target]
    return filtered_words