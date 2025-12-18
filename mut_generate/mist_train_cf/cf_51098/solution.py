"""
QUESTION:
Develop a function called `word_frequency` that takes a string as an input and returns a list of tuples, where each tuple contains a word from the string and its frequency. The function should ignore case, process the string without using built-in word counting features, and present the result in the order of the most frequently occurred word to the least. The function should handle edge cases such as null or empty strings.
"""

def word_frequency(s):
    # Check for null or empty strings
    if not s:
        return "Error: String cannot be null or empty"

    # Remove punctuation and lower case the words
    words = ''.join(e for e in s if (e.isalnum() or e.isspace())).lower().split()

    # Create a dictionary to store words and their frequencies
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    # Sort the dictionary by value in descending order and convert to list
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_count