"""
QUESTION:
Write a function `alphabetical_sort` that takes a list of words as input and returns the list sorted in descending order based on the alphabetical value of each word. The alphabetical value of a word is calculated by summing the positions of its letters in the alphabet (A=1, B=2, ..., Z=26). If two words have the same alphabetical value, maintain their original sequence.
"""

def alphabetical_sort(words):
    """
    Sorts a list of words in descending order based on their alphabetical value.
    
    The alphabetical value of a word is calculated by summing the positions of its letters in the alphabet (A=1, B=2, ..., Z=26).
    If two words have the same alphabetical value, their original sequence is maintained.
    
    Args:
        words (list): A list of words to be sorted.
    
    Returns:
        list: The sorted list of words.
    """
    return sorted(words, key=lambda word: sum(ord(char.lower()) - 96 for char in word if char.isalpha()), reverse=True)