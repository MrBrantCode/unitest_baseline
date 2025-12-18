"""
QUESTION:
Implement a function named `word_frequency` that takes a string as input and returns a list of tuples, where each tuple contains a word and its frequency. The function should ignore punctuation, convert all words to lowercase, and sort the words in descending order based on their frequency. In case of a tie, sort the words alphabetically. Do not use any built-in functions or libraries for counting the frequency of words.
"""

def word_frequency(string):
    # Remove punctuation and convert to lowercase
    string = string.lower()
    string = ''.join(e for e in string if e.isalnum() or e.isspace())
    
    # Split the string into a list of words
    words = string.split()
    
    # Create a dictionary to store the frequency of each word
    frequency = {}
    
    # Count the frequency of each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    # Sort the dictionary by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_frequency