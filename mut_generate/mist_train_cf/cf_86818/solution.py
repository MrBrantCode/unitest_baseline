"""
QUESTION:
Write a function named `get_word_frequencies` that takes a string of up to 10^6 characters as input. The string can contain lowercase letters, spaces, special characters, and uppercase letters. The function should return a dictionary containing the frequencies of each word in the string, but only include words that have a frequency greater than 2. The function should be able to handle duplicate words and consider them as separate entities, and it should run in O(n) time complexity, where n is the length of the input string.
"""

def get_word_frequencies(string):
    # Split the input string into words
    words = string.split()
    
    # Initialize an empty dictionary to store word frequencies
    frequencies = {}
    
    # Iterate through each word and update its frequency in the dictionary
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    
    # Split the final frequencies dictionary into two dictionaries:
    # one for words with frequency greater than 2 and one for the rest
    frequent_words = {word: count for word, count in frequencies.items() if count > 2}
    
    # Return the frequent words dictionary
    return frequent_words