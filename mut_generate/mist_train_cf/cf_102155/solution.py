"""
QUESTION:
Write a function `check_word_presence` that checks if a specific word is present in a given sentence. The function should be case-insensitive and detect variations of the word, such as plurals or different tenses. The function should return a string indicating whether the word is present or not.

The function should take two parameters: `target_word` (the word to be searched) and `sentence` (the sentence to search in).
"""

def check_word_presence(target_word, sentence):
    """
    Checks if a specific word is present in a given sentence.
    
    The function is case-insensitive and detects variations of the word, 
    such as plurals or different tenses.
    
    Args:
        target_word (str): The word to be searched.
        sentence (str): The sentence to search in.
    
    Returns:
        str: A string indicating whether the word is present or not.
    """
    # Convert the given sentence to lowercase
    lowercase_sentence = sentence.lower()
    
    # Split the lowercase sentence into a list of words
    words = lowercase_sentence.split()
    
    # Iterate over each word in the list
    for word in words:
        # Check if the current word is equal to the target word
        if word == target_word.lower():
            # If the current word is equal to the target word, return the message
            return f"The word {target_word} is present in the given sentence"
    
    # If none of the words in the list match the target word, return the message
    return f"The word {target_word} is not present in the given sentence"