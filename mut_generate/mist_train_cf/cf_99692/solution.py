"""
QUESTION:
Replace the first `n` occurrences of words in a given text with their opposites. 

Function name: replace_words_with_opposites

Input: 
- `text`: the original text
- `n`: the number of words to replace
- `word_replacements`: a dictionary of word replacements where the keys are the original words and the values are their opposites

Output: 
- The modified text with the first `n` occurrences of the words replaced with their opposites.

Restriction: 
- Only replace the exact word matches as specified in the `word_replacements` dictionary.
"""

def replace_words_with_opposites(text, n, word_replacements):
    """
    Replace the first n occurrences of words in a given text with their opposites.

    Args:
        text (str): The original text.
        n (int): The number of words to replace.
        word_replacements (dict): A dictionary of word replacements where the keys are the original words and the values are their opposites.

    Returns:
        str: The modified text with the first n occurrences of the words replaced with their opposites.
    """
    words = text.split()
    num_replaced = 0
    for i in range(len(words)):
        if words[i] in word_replacements:
            words[i] = word_replacements[words[i]]
            num_replaced += 1
        if num_replaced == n:
            break
    return " ".join(words)