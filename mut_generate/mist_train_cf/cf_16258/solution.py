"""
QUESTION:
Write a function named `count_words_with_vowel_start` that takes a string and an integer as arguments and returns the number of words in the string that start with a vowel and are of the provided length. The input string can contain multiple sentences and punctuations.
"""

def count_words_with_vowel_start(string, length):
    # Define a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Split the string into words
    words = string.split()
    
    # Initialize a counter for the number of words that meet the criteria
    count = 0
    
    # Iterate over each word
    for word in words:
        # Remove punctuation from the word
        word = ''.join(e for e in word if e.isalnum() or e.isspace())
        
        # Check if the word starts with a vowel and has the desired length
        if word[0].lower() in vowels and len(word) == length:
            count += 1
    
    return count