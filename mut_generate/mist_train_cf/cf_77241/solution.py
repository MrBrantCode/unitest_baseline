"""
QUESTION:
Write a function `replace_odd_indexed_chars(sentence, target)` that replaces every odd-indexed character in the target word with '#' in a given sentence. The function should treat different occurrences of the target word individually and preserve any punctuation that may be attached to the target word.
"""

def replace_odd_indexed_chars(sentence, target):
    """
    Replaces every odd-indexed character in the target word with '#' in a given sentence.
    
    Args:
        sentence (str): The input sentence.
        target (str): The target word.
    
    Returns:
        str: The modified sentence.
    """
    words = sentence.split()
    for i, word in enumerate(words):
        if word.strip(",.") == target:  
            new_word = "".join([c if j % 2 == 0 else "#" for j, c in enumerate(word)])
            words[i] = new_word  
    return " ".join(words)