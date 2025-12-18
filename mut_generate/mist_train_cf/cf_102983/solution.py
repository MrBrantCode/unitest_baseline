"""
QUESTION:
Create a function `create_reverse_lookup` that takes a list of words as input and returns a dictionary where each word containing at least one vowel is a key, and its corresponding value is a list of indices where the word appears in the input list. The function should be case-insensitive.
"""

def create_reverse_lookup(words):
    """
    Creates a reverse lookup dictionary where each word containing at least one vowel is a key,
    and its corresponding value is a list of indices where the word appears in the input list.
    
    Args:
    words (list): A list of words.
    
    Returns:
    dict: A dictionary where each key is a word containing at least one vowel, and its value is a list of indices.
    """
    
    reverse_lookup = {}
    
    for index, word in enumerate(words):
        # Convert the word to lowercase to ignore case sensitivity
        word = word.lower()
        
        # Check if the word contains at least one vowel
        if any(char in 'aeiou' for char in word):
            # If the word contains a vowel, add it to the reverse lookup dictionary
            if word in reverse_lookup:
                reverse_lookup[word].append(index)
            else:
                reverse_lookup[word] = [index]
                
    return reverse_lookup