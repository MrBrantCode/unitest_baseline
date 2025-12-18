"""
QUESTION:
Write a function named `remove_similar_duplicates` that takes a list of phrases as input and returns a list of unique phrases. The function should consider two phrases similar if they contain the same first word. The input list can contain phrases with multiple words separated by spaces. The output list should contain the unique phrases separated by commas.
"""

def remove_similar_duplicates(phrases):
    """
    This function takes a list of phrases as input, removes similar duplicates 
    based on the first word of each phrase, and returns a list of unique phrases.

    Args:
    phrases (list): A list of phrases.

    Returns:
    list: A list of unique phrases.
    """
    unique_phrases = set()
    result = []

    for phrase in phrases:
        first_word = phrase.split()[0]
        if first_word not in unique_phrases:
            unique_phrases.add(first_word)
            result.append(phrase)

    return result