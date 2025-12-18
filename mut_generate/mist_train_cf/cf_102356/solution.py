"""
QUESTION:
Write a function `filter_and_sort_words` to filter a given list of words and return a new list containing only the words that start with "T" and contain the letter "e", sorted in reverse alphabetical order. The time complexity of the solution should be O(n log n), where n is the number of words in the given list.
"""

def filter_and_sort_words(words_list):
    """
    This function filters a given list of words and returns a new list containing 
    only the words that start with 'T' and contain the letter 'e', sorted in 
    reverse alphabetical order.

    Args:
        words_list (list): The list of words to be filtered and sorted.

    Returns:
        list: A new list of words that meet the specified conditions, sorted in 
        reverse alphabetical order.
    """
    return sorted([word for word in words_list if word.startswith('T') and 'e' in word], reverse=True)