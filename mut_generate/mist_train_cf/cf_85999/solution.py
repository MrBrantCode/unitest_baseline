"""
QUESTION:
Implement the `count_unique_words` function to count unique words in a given text while ignoring case differences and excluding a list of specified stop words. The function should take three parameters: `text` (the input string), `exclude_stop_words` (a boolean indicating whether to exclude stop words), and `stop_words_list` (a list of words to exclude). If `exclude_stop_words` is `False` or `stop_words_list` is `None`, the function should count all unique words in the text.
"""

def count_unique_words(text, exclude_stop_words=False, stop_words_list=None):
    """
    Count unique words in a given text while ignoring case differences and excluding a list of specified stop words.

    Args:
        text (str): The input string.
        exclude_stop_words (bool): A boolean indicating whether to exclude stop words. Defaults to False.
        stop_words_list (list): A list of words to exclude. Defaults to None.

    Returns:
        int: The number of unique words in the text.
    """
    words = text.lower().split()
    count = set()
    
    if exclude_stop_words and stop_words_list is not None:
        for word in words:
            if word not in stop_words_list:
                count.add(word)
    else:
        count = set(words)
        
    return len(count)