"""
QUESTION:
Write a function `convert_and_sort(words)` that takes a list of words as input, removes any duplicates, removes words starting with a vowel, and returns the resulting list in reverse alphabetical order.
"""

def convert_and_sort(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    unique_words = set(words)
    filtered_words = {word for word in unique_words if word[0].lower() not in vowels}
    sorted_words = sorted(filtered_words, reverse=True)
    return sorted_words