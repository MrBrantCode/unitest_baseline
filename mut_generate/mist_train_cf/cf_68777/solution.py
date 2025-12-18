"""
QUESTION:
Write a function named `word_count` that takes a text string, an array of words, and an array of stop words as input, and returns a dictionary containing the number of occurrences of each word in the array, excluding stop words. The function should remove punctuation from the text string, and consider case sensitivity by converting the text and words to lowercase before processing. The function should ignore words that are in the stop words array.
"""

from collections import Counter
import re

def word_count(text_string, word_array, stop_words):
    """
    Returns a dictionary containing the number of occurrences of each word in the array, 
    excluding stop words.

    Parameters:
    text_string (str): Input text string.
    word_array (list): Array of words to be counted.
    stop_words (list): Array of stop words to be excluded.

    Returns:
    dict: Dictionary containing the word counts.
    """
    text_string_nopunct = re.sub(r'[^\w\s]', '', text_string)
    text_list = text_string_nopunct.lower().split() 
    filtered_text = [word for word in text_list if word not in [stop_word.lower() for stop_word in stop_words]] 
    count_words = Counter(filtered_text)

    word_dict = {word.lower(): count_words[word] for word in word_array if word.lower() not in [stop_word.lower() for stop_word in stop_words]}

    return word_dict