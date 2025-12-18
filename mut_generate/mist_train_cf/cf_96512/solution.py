"""
QUESTION:
Write a function `reverse_words` that takes a string as input, extracts the second half of the string (split into words), reverses the order of characters in each word, and returns the reversed words separated by commas.
"""

def reverse_words(string):
    # Split the string into words
    words = string.split()

    # Calculate the index to split the words
    split_index = len(words) // 2

    # Get the second half of the words
    second_half = words[split_index:]

    # Reverse the order of characters in each word
    reversed_words = [word[::-1] for word in second_half]

    # Join the reversed words with a comma
    output = ",".join(reversed_words)

    return output