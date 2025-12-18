"""
QUESTION:
Write a function named `find_word(sentence, word)` to find the index of the given word in the sentence. The sentence should contain at least 15 words and not exceed a maximum length of 150 characters. The word should only be considered a match if it appears as a complete word, not as part of another word. The comparison should be case-insensitive. The function should return the index of the word if found, otherwise return -1.
"""

def find_word(sentence, word):
    """
    Find the index of a given word in a sentence.

    Args:
    sentence (str): The sentence to search in (at least 15 words, max 150 characters).
    word (str): The word to search for.

    Returns:
    int: The index of the word if found, -1 otherwise.

    """
    # Ensure the sentence and word are in lowercase for case-insensitive comparison
    sentence = sentence.lower()
    word = word.lower()

    # Split the sentence into a list of words
    words = sentence.split(" ")

    # Iterate over the list of words and check for a match
    for i in range(len(words)):
        if words[i] == word:
            # Return the index if the word is found
            return i

    # Return -1 if the word is not found
    return -1