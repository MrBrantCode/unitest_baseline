"""
QUESTION:
Write a function `filter_sentences` that takes a 2D list of sentences `paragraphs` as input. The function should return a list of sentences where each sentence contains 10 words or less and has an average word length of 5 or less. Optimize the solution for memory usage.
"""

def filter_sentences(paragraphs):
    """
    Filter sentences in a 2D list to include only those with 10 words or less and an average word length of 5 or less.

    Args:
        paragraphs (list): A 2D list of sentences.

    Returns:
        list: A list of filtered sentences.
    """
    # Flatten the list
    flat_paragraphs = [sentence for sublist in paragraphs for sentence in sublist]

    # Filter out the sentences with more than 10 words or average word length > 5
    filtered_paragraphs = [sentence for sentence in flat_paragraphs 
                          if len(sentence.split()) <= 10 
                          and (sum(len(word) for word in sentence.split()) / len(sentence.split())) <= 5]

    return filtered_paragraphs