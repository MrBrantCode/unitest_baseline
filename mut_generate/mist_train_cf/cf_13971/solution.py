"""
QUESTION:
Write a function `alphabet_frequency` that takes a string `sentence` as input and returns a dictionary containing the frequencies of all English alphabets in the sentence. The function should treat uppercase and lowercase letters as different characters and ignore punctuation marks and other non-alphabet characters.
"""

def alphabet_frequency(sentence):
    """
    This function calculates the frequency of English alphabets in a given sentence.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        dict: A dictionary containing the frequencies of all English alphabets in the sentence.
    """
    frequency = {}
    
    for char in sentence:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
                
    return frequency