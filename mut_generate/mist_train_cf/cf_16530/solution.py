"""
QUESTION:
Write a function `remove_words` that takes an array of strings and a single character as input, and returns a new array containing only the words that do not contain the specified character, regardless of case.
"""

def remove_words(arr, letter):
    result = []
    for word in arr:
        if letter.lower() not in word.lower():
            result.append(word)
    return result