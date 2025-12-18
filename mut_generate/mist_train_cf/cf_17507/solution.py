"""
QUESTION:
Create a function `create_reverse_dict` that takes a list of words as input and returns a dictionary where the keys are words containing at least two vowels (case insensitive) and the values are lists of indices where the word appears in the original list.
"""

def create_reverse_dict(words):
    """
    Create a dictionary where keys are words containing at least two vowels 
    (case insensitive) and the values are lists of indices where the word 
    appears in the original list.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary with words containing at least two vowels as keys 
              and their indices as values.
    """
    reverse_dict = {}
    
    for index, word in enumerate(words):
        # Convert the word to lowercase for case insensitivity
        lowercase_word = word.lower()
        
        # Count the number of vowels in the word
        vowel_count = sum(1 for char in lowercase_word if char in 'aeiou')
        
        # Check if the word contains at least two vowels
        if vowel_count >= 2:
            # Add the word and its index to the reverse lookup dictionary
            if lowercase_word in reverse_dict:
                reverse_dict[lowercase_word].append(index)
            else:
                reverse_dict[lowercase_word] = [index]
                
    return reverse_dict