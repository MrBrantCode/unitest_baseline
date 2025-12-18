"""
QUESTION:
Write a function `convert_string(string)` that takes a string of lowercase alphabets without punctuation as input, and returns a list of words that do not start with a vowel, sorted in descending order of word length, with no duplicates. The time complexity should be O(n log n), where n is the length of the input string.
"""

def convert_string(string):
    words = string.split()
    unique_words = set()
    result = []

    for word in words:
        if not word[0] in 'aeiou':
            if not word in unique_words:
                result.append(word)
                unique_words.add(word)

    result = sorted(result, key=len, reverse=True)
    return result