"""
QUESTION:
Write a function `find_shortest_sentence` that takes a list of sentences as input, and returns the sentence with the shortest length, where length is calculated by adding the number of words and the number of characters (excluding punctuation) in the sentence.
"""

import string

def find_shortest_sentence(sentences):
    """
    This function takes a list of sentences as input and returns the sentence with the shortest length.
    Length is calculated by adding the number of words and the number of characters (excluding punctuation) in the sentence.

    Args:
        sentences (list): A list of sentences.

    Returns:
        str: The sentence with the shortest length.
    """

    sentence_dict = {}

    for sentence in sentences:
        # Removing punctuation
        sentence_no_punctuation = sentence.translate(str.maketrans('', '', string.punctuation))

        # Splitting into words and counting them
        word_count = len(sentence_no_punctuation.split())

        # Counting characters
        char_count = len(sentence_no_punctuation.replace(" ", ""))

        # Factoring in the number of words and characters
        sentence_length = word_count + char_count

        # Storing in dictionary
        sentence_dict[sentence] = sentence_length

    # Finding the sentence with the least length
    return min(sentence_dict, key=sentence_dict.get)