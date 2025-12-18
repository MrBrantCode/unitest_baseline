"""
QUESTION:
Write a function `sentence_lengths(sentences)` that takes a list of sentences as input and returns the shortest sentence, its percentage of total characters, the longest sentence, and its percentage of total characters. The total characters should include spaces and punctuation marks. The percentage is calculated based on the total number of characters in all sentences.
"""

def sentence_lengths(sentences):
    """
    Calculate the shortest sentence, its percentage of total characters, 
    the longest sentence, and its percentage of total characters.

    Args:
        sentences (list): A list of sentences.

    Returns:
        tuple: A tuple containing the shortest sentence, its percentage of total characters, 
        the longest sentence, and its percentage of total characters.
    """
    # Calculating the total number of characters
    total_chars = sum(len(sentence) for sentence in sentences)

    # Initialize the variables to store the shortest and longest sentences
    shortest = sentences[0]
    longest = sentences[0]

    # Loop through the sentences to find the shortest and longest
    for sentence in sentences:
        if len(sentence) < len(shortest):
            shortest = sentence
        if len(sentence) > len(longest):
            longest = sentence

    # Calculating the percentage of total characters
    shortest_percent = (len(shortest) / total_chars) * 100
    longest_percent = (len(longest) / total_chars) * 100

    return shortest, shortest_percent, longest, longest_percent