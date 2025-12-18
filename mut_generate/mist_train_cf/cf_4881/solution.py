"""
QUESTION:
Write a function `count_ed_words` that takes a string of text as input. The function should return the count of words that start with a vowel, contain the string "ed", and have at least one consonant after the "ed". Vowels are defined as 'a', 'e', 'i', 'o', 'u', and consonants are defined as all letters that are not vowels.
"""

def count_ed_words(text):
    """
    This function counts the number of words in a given text that start with a vowel, 
    contain the string "ed", and have at least one consonant after the "ed".

    Parameters:
    text (str): The input text.

    Returns:
    int: The count of words that meet the specified conditions.
    """
    
    # Define vowels and consonants
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # Split the text into words
    words = text.split()
    
    # Initialize a counter for the words that meet the conditions
    count = 0
    
    # Iterate over each word in the text
    for word in words:
        # Check if the word starts with a vowel and contains 'ed'
        if word[0].lower() in vowels and 'ed' in word:
            # Find the index of 'ed' in the word
            ed_index = word.index('ed')
            
            # Check if there's at least one consonant after 'ed'
            if any(char.lower() in consonants for char in word[ed_index + 2:]):
                # If the word meets all conditions, increment the counter
                count += 1
                
    # Return the count of words that meet the conditions
    return count