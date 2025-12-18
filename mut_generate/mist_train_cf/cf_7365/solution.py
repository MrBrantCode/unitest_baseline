"""
QUESTION:
Create a function `search_words` that takes a sentence as input and returns a list of words that start with "th", are longer than seven characters, and contain at least two vowels.
"""

def search_words(sentence):
    """
    This function searches for words in a given sentence that start with "th", 
    are longer than seven characters, and contain at least two vowels.

    Args:
    sentence (str): The input sentence to be searched.

    Returns:
    list: A list of words that match the specified criteria.
    """
    
    # Define the vowels
    vowels = 'aeiou'
    
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize an empty list to store the matching words
    matching_words = []
    
    # Iterate over each word in the sentence
    for word in words:
        # Check if the word starts with 'th' and is longer than 7 characters
        if word.startswith('th') and len(word) > 7:
            # Initialize a counter for vowels in the word
            vowel_count = 0
            
            # Iterate over each character in the word
            for char in word:
                # Check if the character is a vowel
                if char.lower() in vowels:
                    # Increment the vowel count
                    vowel_count += 1
            
            # Check if the word contains at least 2 vowels
            if vowel_count >= 2:
                # Add the word to the list of matching words
                matching_words.append(word)
    
    # Return the list of matching words
    return matching_words