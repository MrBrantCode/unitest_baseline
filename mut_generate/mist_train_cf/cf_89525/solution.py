"""
QUESTION:
Create a function `categorize_phrases(phrases, categories)` that takes in a list of phrases and a list of corresponding categories, and returns a dictionary where each phrase is mapped to its corresponding category. The function should have a time complexity of O(n), where n is the number of phrases. Each phrase can only belong to one category, and each category must contain at least one phrase. The total number of characters in all phrases combined is at most 10^6, and the total number of phrases and categories combined is at most 10^4.
"""

def categorize_phrases(phrases, categories):
    """
    Maps phrases to their corresponding categories.

    Args:
    phrases (list): A list of phrases.
    categories (list): A list of categories corresponding to the phrases.

    Returns:
    dict: A dictionary where each phrase is mapped to its corresponding category.

    Time complexity: O(n), where n is the number of phrases.
    """
    return {phrase: category for phrase, category in zip(phrases, categories)}