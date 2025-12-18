"""
QUESTION:
Write a function called `remove_redundant_words` that takes a sentence as input and returns a new sentence with all redundant words removed. The function should consider a word as redundant if it appears more than once in the original sentence. The order of the words in the original sentence should be preserved.
"""

def remove_redundant_words(sentence):
    """
    Removes redundant words from a sentence, preserving the original order.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The sentence with all redundant words removed.
    """
    words = sentence.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return " ".join(unique_words)