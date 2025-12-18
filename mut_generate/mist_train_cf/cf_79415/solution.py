"""
QUESTION:
Write a function named `find_max` that takes a list of non-repetitive string characters as input and returns the term with the maximum number of unique characters without considering letter case. If multiple words have the same distinct character count, the function should favor the word appearing first alphabetically. The function should have a linear time complexity (O(n)).
"""

def find_max(words):
    """ Finds the word from a list with the maximum number of unique letters
    
    Args:
        words (List[str]): list of words

    Returns:
        str : the word with maximum unique letters. 
        If there are multiple such words, the one appearing first alphabetically

    """

    max_word = ''
    max_unique_chars = 0
    
    for word in words:
        unique_chars = set(word.lower())
        num_unique_chars = len(unique_chars)

        if num_unique_chars == max_unique_chars:
            if word.lower() < max_word.lower():
                max_word = word
        elif num_unique_chars > max_unique_chars:
            max_word = word
            max_unique_chars = num_unique_chars

    return max_word