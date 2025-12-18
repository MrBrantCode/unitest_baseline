"""
QUESTION:
Write a function `replace_word` that replaces all occurrences of a target word in a given text with a specified replacement word. The function should take three parameters: `original_text`, `target_word`, and `replacement_word`, and return the modified text. The function should be case-sensitive and consider word boundaries (i.e., it should not replace parts of other words).
"""

def replace_word(original_text, target_word, replacement_word):
    """
    This function replaces all occurrences of a target word 
    in the original text with a replacement word.

    :param original_text: The original text.
    :type original_text: str
    :param target_word: The word to be replaced.
    :type target_word: str
    :param replacement_word: The word to replace the target word.
    :type replacement_word: str
    :return: The text with all occurrences of the target word replaced.
    :rtype: str
    """
    replaced_text = original_text.replace(target_word, replacement_word)
    
    return replaced_text