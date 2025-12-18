"""
QUESTION:
Write a Python function `remove_repeated_words` that takes a string `sentence` as input. The function should return a string where all repeated words are removed from the sentence, regardless of their position and case, and ignoring punctuation marks. The returned string should be in lower case.
"""

def remove_repeated_words(sentence):
    """
    This function removes repeated words from a sentence, 
    regardless of their position and case, and ignoring punctuation marks.
    
    Parameters:
    sentence (str): The input sentence.
    
    Returns:
    str: A string where all repeated words are removed from the sentence in lower case.
    """
    
    # Convert the sentence to lower case and remove punctuation marks
    sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace()).lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Create an empty list to store the unique words
    unique_words = []
    
    # Iterate through each word in the sentence
    for word in words:
        # Check if the word is already in the unique_words list
        if word not in unique_words:
            # If the word is not repeated, add it to the unique_words list
            unique_words.append(word)
    
    # Join the unique words with a space between them to form the final sentence
    final_sentence = ' '.join(unique_words)
    
    return final_sentence