"""
QUESTION:
Write a function named `is_bored` that takes a string `S` as input. The function should count the number of sentences in `S` that start with "I". Sentences are separated by '.', '?' or '!'. The function should return the count of such sentences.
"""

def is_bored(S):
    """
    This function counts the number of sentences in a given string S that start with "I".
    Sentences are separated by '.', '?' or '!'.

    Parameters:
    S (str): The input string containing one or more sentences.

    Returns:
    int: The count of sentences starting with "I".
    """
    # Split the text into sentences
    sentences = []
    temp_sentence = ''
    for char in S:
        if char not in '.?!':
            temp_sentence += char
        else:
            sentences.append(temp_sentence.strip())
            temp_sentence = ''
    sentences.append(temp_sentence.strip())  # Append the last sentence

    # Count the number of boredoms starting with "I"
    boredom_count = 0
    for sentence in sentences:
        if len(sentence) > 0 and sentence[0] == 'I':
            boredom_count += 1

    return boredom_count