"""
QUESTION:
Write a function `convert_and_sort` that takes a list of words as input. The function should convert the list into a set to remove any duplicate elements, sort the resulting set in reverse alphabetical order, and remove any words that start with a vowel (both lowercase and uppercase). The function should return the resulting list of words.
"""

def convert_and_sort(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    unique_words = set(words)
    filtered_words = {word for word in unique_words if word[0].lower() not in vowels}
    sorted_words = sorted(filtered_words, reverse=True)
    return sorted_words