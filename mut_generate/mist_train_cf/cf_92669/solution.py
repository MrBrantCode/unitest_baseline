"""
QUESTION:
Create a function `process_word_list` that takes a list of words as input. The function should use multithreading or multiprocessing to calculate the length of each word in the list in parallel. The function should then return a dictionary containing the length of each word, but only include words that have at least 5 characters. The dictionary should be sorted in descending order based on the word lengths.
"""

import concurrent.futures

def process_word_list(words):
    # Function to process each word and return its length
    def process_word(word):
        return len(word)

    # Create a thread pool executor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Process each word in parallel
        word_lengths = list(executor.map(process_word, words))

    # Create a dictionary containing word lengths
    word_lengths_dict = dict(zip(words, word_lengths))

    # Filter words with at least 5 characters
    filtered_dict = {word: length for word, length in word_lengths_dict.items() if length >= 5}

    # Sort the dictionary in descending order based on the number of characters
    sorted_dict = dict(sorted(filtered_dict.items(), key=lambda x: x[1], reverse=True))

    return sorted_dict