"""
QUESTION:
Create a function called `process_string` that takes an input string, converts all words to upper case, removes duplicates, and sorts the words in descending order based on their length. The function should return a string with the processed words separated by spaces.
"""

def process_string(input_str):
    words = input_str.upper().split()
    unique_words = set(words)
    sorted_words = sorted(unique_words, key=len, reverse=True)
    return ' '.join(sorted_words)