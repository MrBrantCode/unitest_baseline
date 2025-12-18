"""
QUESTION:
Write a function called `find_shortest_sentence` that takes an array of sentences as input and returns the shortest sentence. The function should be able to handle any array of strings. There are no restrictions on the characters used in the strings, and punctuation is considered part of the sentence. The function should return the first shortest sentence it encounters in case of a tie.
"""

def find_shortest_sentence(sentences):
    """
    This function takes an array of sentences as input and returns the shortest sentence.
    
    Parameters:
    sentences (list): A list of strings representing the sentences.
    
    Returns:
    str: The shortest sentence in the input list.
    """
    if not sentences:
        return ""
    
    min_length = len(sentences[0])
    min_sentence = sentences[0]

    for sentence in sentences:
        if len(sentence) < min_length:
            min_length = len(sentence)
            min_sentence = sentence

    return min_sentence