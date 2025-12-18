"""
QUESTION:
Write a function `count_words(string)` that counts the number of words in a given string, ignoring any occurrences of "test" and its variations ("testing", "tested", etc.), and handles both uppercase and lowercase variations of the word "test". The function should have a time complexity of O(n), where n is the length of the string.
"""

def count_words(string):
    count = 0
    words = string.lower().split()
    for word in words:
        if word not in ['test', 'testing', 'tested', 'tests']:
            count += 1
    return count