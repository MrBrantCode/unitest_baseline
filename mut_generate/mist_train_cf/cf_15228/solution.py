"""
QUESTION:
Implement a function `extract_last_three_words` that takes a string of at least five words, separated by single spaces, and returns the last three words. The function should ignore leading or trailing spaces and return an empty list if the string contains less than five words. The time complexity should be O(n), where n is the length of the input string.
"""

def extract_last_three_words(input_string):
    input_string = input_string.strip()
    words = input_string.split()
    if len(words) < 5:
        return []
    return words[-3:]