"""
QUESTION:
Write a function `solve(words)` that takes a list of strings as input and returns a list of strings sorted in lexicographically descending order, grouped by fruit and non-fruit categories. Fruits are predefined as "kiwi", "melon", "orange", "apple", "banana", "peach", "grape", "cherry", "mango", and "pineapple". If multiple words belong to the same category, they should maintain the reverse lexicographical order within their own category. The function should also include a helper function `is_fruit(word)` that identifies whether a word is a fruit.
"""

def is_fruit(word):
    """Checks if a word is a fruit."""
    fruits = ["kiwi", "melon", "orange", "apple", "banana", "peach", "grape", "cherry", "mango", "pineapple"]
    return word in fruits

def solve(words):
    """
    Sorts a list of strings in lexicographically descending order, 
    grouped by fruit and non-fruit categories.

    Args:
        words (list): A list of strings

    Returns:
        list: A list of strings sorted in lexicographically descending order
    """
    words.sort(key=lambda x: (not is_fruit(x), x), reverse=True)
    return words