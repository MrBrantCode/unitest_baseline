"""
QUESTION:
Write a function `count_words` that takes a string of words and an integer `N` as input. The function should return a dictionary where the keys are unique words from the string and the values are their frequencies, as well as a list of the top `N` words with the highest frequency in descending order. The function should ignore case sensitivity and word order.
"""

def count_words(s, N):
    """
    Returns a dictionary of word frequencies and a list of top N words.

    Args:
    s (str): The input string of words.
    N (int): The number of top words to return.

    Returns:
    dict: A dictionary where keys are unique words and values are their frequencies.
    list: A list of top N words with the highest frequency in descending order.
    """
    # Convert the string to lower case and split it into words
    words = s.lower().split()
    
    # Create a dictionary to store the frequency of each word
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    # Sort the dictionary by frequency in descending order and get the top N words
    top_N_words = sorted(freq_dict, key=freq_dict.get, reverse=True)[:N]

    return freq_dict, top_N_words