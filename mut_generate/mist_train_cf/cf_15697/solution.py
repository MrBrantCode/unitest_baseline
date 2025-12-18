"""
QUESTION:
Create a function that takes a string of text and a boolean indicating whether to sort in reverse order as input. The function should return a tuple containing the text with unique words in alphabetical order (or reverse alphabetical order if specified) and the total number of unique words. The input string is assumed to be space-separated words.
"""

def process_text(text, reverse_sort):
    """
    This function takes a string of text and a boolean indicating whether to sort in reverse order as input.
    It returns a tuple containing the text with unique words in alphabetical order (or reverse alphabetical order if specified) and the total number of unique words.

    Args:
        text (str): The input string of text.
        reverse_sort (bool): A boolean indicating whether to sort in reverse order.

    Returns:
        tuple: A tuple containing the modified text and the total number of unique words.
    """

    # Splitting the input text into individual words
    words = text.split()

    # Removing duplicate words and sorting in alphabetical order
    unique_words = sorted(set(words))

    # Reversing the unique words if reverseSort is True
    if reverse_sort:
        unique_words = unique_words[::-1]

    # Joining the unique words back into a string
    modified_text = ' '.join(unique_words)

    # Returning the modified text and the total number of unique words
    return modified_text, len(unique_words)