"""
QUESTION:
Create a function named `find_word_indices` that takes a list of sentences and a word as input. The function should traverse through the sentences, locate all occurrences of the specified word, and print the word's index upon encountering it. The function should return the indices of the word's appearances, if any, and should not match the word if it is part of another word.
"""

def find_word_indices(sentences, word):
    """
    This function finds all occurrences of a word in a list of sentences.
    
    Parameters:
    sentences (list): A list of sentences.
    word (str): The word to be searched.
    
    Returns:
    list: A list of tuples containing the sentence index and word index of each occurrence.
    """
    indices = []
    for idx, sentence in enumerate(sentences):
        words = sentence.split()
        for i, w in enumerate(words):
            if w == word:
                indices.append((idx, i))
                print(f"In sentence {idx+1}, '{word}' is found at word index {i+1}.")
    return indices