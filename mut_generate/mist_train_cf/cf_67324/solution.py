"""
QUESTION:
Implement a function `process_words` that takes in three parameters: `words` (a list of strings), `target_char` (a character), and `target_word` (a string). This function should return the index of `target_word` in `words` and the index of `target_char` within `target_word`. It should also return the count of `target_char` in `target_word`. If `target_char` is not found in `words`, the function should indicate this. The function should be case-sensitive and handle non-alphabetic symbols.
"""

def process_words(words, target_char, target_word):
    """
    This function takes in three parameters: a list of strings, a target character, and a target word.
    It returns the index of the target word in the list, the index of the target character within the target word,
    and the count of the target character in the target word. If the target character is not found, it indicates this.

    Parameters:
    words (list): A list of strings.
    target_char (str): A target character.
    target_word (str): A target word.

    Returns:
    tuple or str: A tuple containing the index of the target word, the index of the target character, and the count of the target character.
                  If the target character is not found, it returns a message indicating this.
    """
    for i, word in enumerate(words):
        if word == target_word:
            char_indexes = [j for j, char in enumerate(word) if char == target_char]
            if char_indexes:
                return (i, char_indexes, len(char_indexes))
            else:
                return f"'{target_char}' not found in '{target_word}'."
    return f"'{target_word}' not found in words collection."