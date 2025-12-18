"""
QUESTION:
Create a function `reverse_lookup_dict` that takes a list of words as input and returns a dictionary where keys are the words (in lowercase) and values are lists of indices where the word appears in the input list. The dictionary should only include words that contain at least two vowels, and the function should ignore case sensitivity.
"""

def reverse_lookup_dict(words):
    """
    Create a dictionary where keys are the words (in lowercase) and values are lists of indices 
    where the word appears in the input list. The dictionary only includes words that contain 
    at least two vowels, and the function ignores case sensitivity.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary where keys are words and values are lists of indices.
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