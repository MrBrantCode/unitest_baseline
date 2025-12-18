"""
QUESTION:
Create a function called `create_reverse_lookup` that takes a list of words as input and returns a dictionary where the keys are the words and the values are lists of indices where each word appears in the input list. The function should only include words that contain at least one vowel and should ignore case sensitivity.
"""

def create_reverse_lookup(words):
    """
    Creates a reverse lookup dictionary from a list of words.
    
    Args:
    words (list): A list of words.
    
    Returns:
    dict: A dictionary where the keys are the words and the values are lists of indices where each word appears in the input list.
    """
    
    # Initialize an empty dictionary to store the reverse lookup
    reverse_lookup = {}
    
    # Iterate over the list of words with their indices
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
    
    # Return the reverse lookup dictionary
    return reverse_lookup