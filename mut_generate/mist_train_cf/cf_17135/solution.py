"""
QUESTION:
Create a function `word_counts` that takes a string of multiple sentences as input, returns a dictionary with words and corresponding counts of occurrences of each word, ignores case sensitivity and punctuation marks, excludes any words that are palindromes, and only includes words with a count greater than 2.
"""

import string

def word_counts(text):
    # Remove punctuation marks from the text
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Convert the text to lowercase
    text = text.lower()
    
    # Split the text into words
    words = text.split()
    
    # Initialize an empty dictionary to store word counts
    word_counts = {}
    
    # Loop through each word in the text
    for word in words:
        # Check if the word is a palindrome
        if word == word[::-1]:
            continue
        
        # If the word is not a palindrome, update its count in the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Remove words with a count less than or equal to 2
    word_counts = {word: count for word, count in word_counts.items() if count > 2}
    
    return word_counts