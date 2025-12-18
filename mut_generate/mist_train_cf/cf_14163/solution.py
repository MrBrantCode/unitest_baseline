"""
QUESTION:
Write a function `longest_words` that takes a list of strings as input. The function should return all the longest words in the list, considering different capitalizations as different words. If the list is empty or contains only empty strings, return "Input list is empty or contains only empty strings." The function should have a time complexity of O(n), where n is the total number of characters in the input list.
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