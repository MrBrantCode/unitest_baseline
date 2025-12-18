"""
QUESTION:
Create a function called `reverse_and_remove_duplicates` that takes a list of strings as input, reverses the order of the words, removes any duplicate words, and returns the resulting list. The order of words in the output list should be the reverse of the original list, and there should be no duplicate words. The function should handle any number of input strings.
"""

def reverse_and_remove_duplicates(words):
    # Reverse the order of words
    reversed_words = words[::-1]

    # Remove duplicate words using set and maintain the original order of unique words
    unique_words = []
    for word in reversed_words:
        if word not in unique_words:
            unique_words.append(word)

    return unique_words