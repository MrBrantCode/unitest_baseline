"""
QUESTION:
Create a function named `get_word_frequency` that takes two parameters: a list of words and a list of stop words. The function should return a dictionary where the keys are the unique words in the input list (excluding stop words and ignoring case sensitivity) and the values are their corresponding frequencies. The function should handle cases where the stop words list is dynamically generated from a file and the file does not exist or is empty.
"""

def get_word_frequency(words, stop_words):
    # Create an empty frequency table
    frequency_table = {}
    
    # Convert the stop words list to lowercase
    stop_words = [word.lower() for word in stop_words]
    
    # Iterate through the words list
    for word in words:
        # Convert the word to lowercase
        word = word.lower()
        
        # Check if the word is a stop word
        if word in stop_words:
            continue
        
        # If the word is already in the frequency table, increment its count
        if word in frequency_table:
            frequency_table[word] += 1
        # Otherwise, add the word to the frequency table with a count of 1
        else:
            frequency_table[word] = 1
    
    return frequency_table