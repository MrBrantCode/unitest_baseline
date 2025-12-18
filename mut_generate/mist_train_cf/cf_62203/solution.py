"""
QUESTION:
Create a function `filter_excess_vowels` that takes a list of words as input and returns a new list containing the same words, but with any words that have more than three vowels removed. The function should be case-insensitive when counting vowels and should maintain the original order of words in the list.
"""

def filter_excess_vowels(words):
    """
    Filters a list of words, removing any words that have more than three vowels.

    Args:
        words (list): A list of words.

    Returns:
        list: A new list containing the filtered words.
    """
    vowels = 'aeiou'
    return [word for word in words if sum(1 for char in word.lower() if char in vowels) <= 3]