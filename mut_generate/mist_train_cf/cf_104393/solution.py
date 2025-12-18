"""
QUESTION:
Implement a function `check_string_in_list(word_list, target_word)` that checks if `target_word` is present in `word_list`. The function should take two parameters: `word_list`, a list of strings, and `target_word`, a target string. 

The function has the following constraints:
- The length of `word_list` is in the range of 1 to 10^6.
- The average length of the strings in `word_list` is in the range of 1 to 100.
- The length of `target_word` is in the range of 1 to 100.
- The strings in `word_list` and `target_word` only contain lowercase alphabets.

The function should return `True` if `target_word` is present in `word_list`, and `False` otherwise.
"""

def check_string_in_list(word_list, target_word):
    """
    Checks if target_word is present in word_list.

    Args:
        word_list (list): A list of strings.
        target_word (str): A target string.

    Returns:
        bool: True if target_word is present in word_list, False otherwise.
    """
    return target_word in word_list