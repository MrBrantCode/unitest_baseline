"""
QUESTION:
Write a function named `reverse_third_word` that takes a sentence as input, extracts the third word, reverses it, and returns the reversed word. The function should only consider sentences with at least three words. If the sentence has less than three words, the function should return None or indicate that the sentence does not meet the condition.
"""

def reverse_third_word(sentence):
    """
    Extracts the third word from a sentence, reverses it, and returns the reversed word.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        str or None: The reversed third word if the sentence has at least three words, otherwise None.
    """
    words = sentence.split()
    if len(words) >= 3:
        return words[2][::-1]
    else:
        return None