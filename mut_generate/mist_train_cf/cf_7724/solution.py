"""
QUESTION:
Create a function `count_words(string)` that takes a string as input and returns the number of words in the string, excluding any occurrences of the word "test" and its variations ("testing", "tested", "tests", etc.), regardless of case. The function should have a time complexity of O(n), where n is the length of the string.
"""

def count_words(string):
    count = 0
    words = string.lower().split()
    for word in words:
        if word not in ['test', 'testing', 'tested', 'tests']:
            count += 1
    return count