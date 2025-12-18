"""
QUESTION:
Write a function named `update_words` that takes an array of strings "words" as input. If a word has more than 5 characters, replace it with the reverse of the word, then remove all words with more than 5 characters. Finally, return the updated array sorted in descending order based on the length of the words.
"""

def update_words(words):
    """
    Updates the given array of words by replacing words with more than 5 characters with their reverse,
    removing words with more than 5 characters, and sorting the array in descending order based on word length.

    Args:
        words (list): The array of words to update.

    Returns:
        list: The updated array of words.
    """
    # Reverse words with more than 5 characters and remove them if still longer than 5
    words = [word[::-1] if len(word) > 5 else word for word in words]
    words = [word for word in words if len(word) <= 5]

    # Sort the array in descending order based on word length
    words.sort(key=lambda x: len(x), reverse=True)

    return words