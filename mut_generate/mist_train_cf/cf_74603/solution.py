"""
QUESTION:
Write a function `filter_words(word_list)` that takes a list of words as input and returns a new list containing only the words that include the vowel 'e'. The function should not use list comprehensions or built-in Python functions like `filter()`, `map()`, or `reduce()`, and it should only use a single function to accomplish the task.
"""

def filter_words(word_list):
    filtered_words = []
    for word in word_list:
        if "e" in word:
            filtered_words.append(word)
    return filtered_words