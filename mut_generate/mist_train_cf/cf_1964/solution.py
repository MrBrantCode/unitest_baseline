"""
QUESTION:
Design a function `remove_duplicates(sentence)` to remove all duplicate words from a sentence while preserving the order of the remaining words. The function should be case-sensitive, and the order of the remaining words in the sentence should be the same as the original sentence. The function should have a time complexity of O(n), where n is the length of the sentence, and use only constant extra space, without utilizing any built-in string manipulation functions or data structures.
"""

def remove_duplicates(sentence):
    """
    Removes all duplicate words from a sentence while preserving the order of the remaining words.
    
    Args:
    sentence (str): The input sentence.
    
    Returns:
    str: The modified sentence with no duplicate words.
    """
    modified_sentence = ""
    word_start = 0

    for i in range(len(sentence)):
        if sentence[i] == " " or i == len(sentence) - 1:
            if i == len(sentence) - 1:
                word = sentence[word_start:]
            else:
                word = sentence[word_start:i]
                
            if word not in modified_sentence:
                if modified_sentence:
                    modified_sentence += " "
                modified_sentence += word
            word_start = i + 1

    return modified_sentence