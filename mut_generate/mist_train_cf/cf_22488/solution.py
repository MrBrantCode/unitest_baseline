"""
QUESTION:
Create a function `sort_and_filter_words(dictionary)` that takes a dictionary of words and their frequencies as input. The function should return a new dictionary where words containing special characters or numbers are removed, sorted in descending order based on their frequencies, and with frequencies less than or equal to 10 removed.
"""

def sort_and_filter_words(dictionary):
    # Filtering out words with special characters or numbers
    filtered_dict = {word: freq for word, freq in dictionary.items() if word.isalpha()}

    # Sorting the filtered dictionary by frequency in descending order
    sorted_dict = dict(sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True))

    # Removing words with frequency less than or equal to 10
    final_dict = {word: freq for word, freq in sorted_dict.items() if freq > 10}

    return final_dict