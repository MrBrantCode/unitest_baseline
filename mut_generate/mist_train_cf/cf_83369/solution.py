"""
QUESTION:
Create a function `count_letters` that takes a string of text as input and returns a list of tuples, where each tuple contains a letter from the text and its corresponding count. If multiple letters have the same count, they should be sorted alphabetically in the output list. The function should ignore case and non-alphabetical characters.
"""

def count_letters(text):
    text = text.lower()
    count_dict = {char: text.count(char) for char in text if char.isalpha()}
    sorted_tuples = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_tuples