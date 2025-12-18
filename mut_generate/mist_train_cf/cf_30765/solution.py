"""
QUESTION:
Implement the `top_n_frequent_words` function to find the top N most frequently occurring words in a given string. The function should take a string `s` containing space-separated words and an integer `n` as input, and return a list of tuples, each containing a word and its frequency, sorted in descending order by frequency and then lexicographically if frequencies are the same.
"""

def top_n_frequent_words(s, n):
    # Split the input string into individual words
    s = s.split(' ')
    
    # Create a list of tuples containing each word and its frequency
    counted_words = [(w, s.count(w)) for w in set(s)]
    
    # Sort the list based on frequency in descending order, and then lexicographically
    counted_words.sort(key=lambda x: (-x[1], x[0]))
    
    # Return the top N most frequently occurring words
    return counted_words[:n]