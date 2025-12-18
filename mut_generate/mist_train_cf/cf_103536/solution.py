"""
QUESTION:
Write a function named `remove_duplicate_words` that takes a string `sentence` as input, removes any duplicate words, and returns the number of words in the original sentence and the sentence with duplicates removed. The function should consider words as case-sensitive and preserve the original word order.
"""

def remove_duplicate_words(sentence):
    """
    Removes any duplicate words from a given sentence and returns the number of words in the original sentence and the sentence with duplicates removed.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        tuple: A tuple containing the number of words in the original sentence and the sentence with duplicates removed.
    """
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the number of words
    num_words = len(words)
    
    # Create a list for unique words
    unique_words = []
    
    # Iterate over each word
    for word in words:
        # Check if the word is not already in the unique_words list
        if word not in unique_words:
            # Add the word to the unique_words list
            unique_words.append(word)
    
    # Join the unique words list back into a sentence
    unique_sentence = ' '.join(unique_words)
    
    return num_words, unique_sentence