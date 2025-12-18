"""
QUESTION:
Create a function `longest_non_palindromic_word(text)` that takes a string `text` as input, consisting of alphabetical characters and spaces, and returns the first occurrence of the longest word that is not a palindrome. If there are multiple words with the same length, the function should return the first one it encounters.
"""

def longest_non_palindromic_word(text):
    # Split the text into words
    words = text.split()
    
    # Initialize variables
    longest_word = ""
    longest_length = 0
    
    # Iterate through each word
    for word in words:
        # Check if the word is a palindrome
        if word == word[::-1]:
            continue
        
        # Check if the word is longer than the current longest word
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)
    
    return longest_word