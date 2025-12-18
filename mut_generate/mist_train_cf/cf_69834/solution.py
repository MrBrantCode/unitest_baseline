"""
QUESTION:
Create a function `word_frequency(word, string_list)` that takes a word and a list of strings as input and returns the total frequency of the word in the list of strings. The function should count the occurrences of the word in each string in the list, ignoring the case where the word is part of another word.
"""

def word_frequency(word, string_list):
    count = 0
    for string in string_list:
        # Split the string into words
        words = string.lower().split()
        
        # Count occurrences of the given word
        count += words.count(word.lower())
    
    return count