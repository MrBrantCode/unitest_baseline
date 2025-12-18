"""
QUESTION:
Write a function `find_letters_word` that takes a set of letters and a sentence as input, and returns the first word in the sentence that contains all the letters from the set, ignoring case and duplicates. If no word meets this condition, return an empty string.
"""

def find_letters_word(letters, sentence):
    # Convert the letters and sentence to a set and lowercase for case-insensitive comparison
    letters = set(letter.lower() for letter in letters)
    
    # Split the sentence into words
    words = sentence.lower().split()
    
    # Iterate over each word in the sentence
    for word in words:
        # If the set of letters in the word is a superset of the given letters, return the word
        if letters.issubset(set(word)):
            return word
    
    # If no word meets the condition, return an empty string
    return ""