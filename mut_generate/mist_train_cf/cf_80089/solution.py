"""
QUESTION:
Write a function called `split_string_into_words_and_char_freq` that takes a string as input, splits it into a list of words, and for each word, identifies and stores the frequency of each character (excluding spaces) in a dictionary. The characters in the dictionary should be sorted in ascending order based on their frequency. The function should return a list of words and a list of dictionaries, where each dictionary corresponds to a word and contains the frequency of its characters.
"""

from collections import Counter

def split_string_into_words_and_char_freq(s):
    """
    This function splits a string into a list of words and for each word, 
    identifies and stores the frequency of each character (excluding spaces) 
    in a dictionary. The characters in the dictionary are sorted in ascending 
    order based on their frequency.

    Args:
        s (str): The input string.

    Returns:
        list: A list of words.
        list: A list of dictionaries, where each dictionary corresponds to a word 
              and contains the frequency of its characters.
    """
    words_list = s.split()
    char_freq_list = []
    
    for word in words_list:
        char_freq = Counter(word)
        sorted_char_freq = dict(sorted(char_freq.items(), key=lambda item: item[1]))
        char_freq_list.append(sorted_char_freq)
    
    return words_list, char_freq_list