"""
QUESTION:
Create a function named `longest_words` that takes a list of strings as input and returns a list of the longest words. If multiple words have the same maximum length, return all of them. The function should consider words with different capitalization as different words. If the input list is empty or contains only empty strings, return the message "Input list is empty or contains only empty strings." The function should have a time complexity of O(n), where n is the total number of characters in the input list.
"""

def longest_words(lst):
    if not lst or all(word == '' for word in lst):
        return "Input list is empty or contains only empty strings."

    longest_length = 0
    longest_words = []

    for word in lst:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_words = [word]
        elif len(word) == longest_length:
            longest_words.append(word)

    return longest_words