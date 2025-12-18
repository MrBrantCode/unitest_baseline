"""
QUESTION:
Implement the `search_word` function to find the position of a given word in a string without using built-in string search or matching functions. The function should take two parameters, `string` and `word`, and return the starting position of the word in the string. If the word is not found, return -1. The time complexity should be O(n), where n is the length of the string, and the space complexity should be O(1), without using any additional data structures.
"""

def search_word(string, word):
    """
    Find the position of a given word in a string.

    Args:
        string (str): The input string to search in.
        word (str): The word to search for.

    Returns:
        int: The starting position of the word in the string. Returns -1 if not found.
    """
    string_len = len(string)
    word_len = len(word)

    for i in range(string_len - word_len + 1):
        match = True
        for j in range(word_len):
            if string[i + j] != word[j]:
                match = False
                break
        if match:
            return i

    return -1