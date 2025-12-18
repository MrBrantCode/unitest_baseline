"""
QUESTION:
Create a function named `count_unique_words` that takes a string `text` as input. The function should count the occurrences of each unique word in the text, disregarding punctuation marks and treating the comparison as case-insensitive. It should then return or output the unique words along with their respective counts in alphabetical order. The definition of a word is a sequence of characters separated by spaces.
"""

def count_unique_words(text):
    # Remove punctuation and convert to lowercase
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).lower()
    
    # Split the text into words
    words = text.split()
    
    # Count occurrences of each word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Sort the unique words alphabetically
    unique_words = sorted(word_count.keys())
    
    # Return the unique words and their counts
    result = {}
    for word in unique_words:
        result[word] = word_count[word]
    return result