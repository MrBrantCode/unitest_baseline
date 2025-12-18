"""
QUESTION:
Implement a function named `extract_last_three_words` that takes a string of at least five words separated by a single space as input and returns the last three words as a list. The function should ignore any leading or trailing spaces in the input string and have a time complexity of O(n), where n is the length of the input string. If the input string contains less than five words, return an empty list.
"""

def extract_last_three_words(input_string):
    input_string = input_string.strip()
    words = input_string.split()
    if len(words) < 5:
        return []
    return words[-3:]