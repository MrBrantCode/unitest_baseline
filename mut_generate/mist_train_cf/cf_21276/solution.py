"""
QUESTION:
Write a function `reverse_words` that takes a string of words as input, extracts the second half of the string, reverses the order of characters in each word, and returns the result as a comma-separated string. The function should handle strings with an odd number of words by rounding down to the nearest whole number when determining the midpoint.
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