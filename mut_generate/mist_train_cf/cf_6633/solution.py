"""
QUESTION:
Develop a function `extract_words` that takes a sentence and a letter as input, and returns a list of words from the sentence that begin with the given letter (case-insensitive), have a length of at least 3 characters, and contain at least two vowels.
"""

def extract_words(sentence, letter):
    """
    This function takes a sentence and a letter as input, 
    and returns a list of words from the sentence that begin with the given letter (case-insensitive), 
    have a length of at least 3 characters, and contain at least two vowels.

    Args:
    sentence (str): The input sentence.
    letter (str): The letter to filter words by.

    Returns:
    list: A list of words that match the specified criteria.
    """
    # Convert the sentence to lowercase for case-insensitive matching
    sentence = sentence.lower()
    letter = letter.lower()
    
    # Initialize an empty list to store the words that match the criteria
    matching_words = []

    # Split the sentence into words
    words = sentence.split()

    # Iterate over each word in the sentence
    for word in words:
        # Check if the word starts with the specific letter and has a length greater than or equal to 3
        if word.startswith(letter) and len(word) >= 3:
            # Initialize a counter for vowels in the word
            vowel_count = 0
            # Iterate over each character in the word
            for char in word:
                # Check if the character is a vowel
                if char in "aeiou":
                    # Increment the vowel count
                    vowel_count += 1
            # Check if the word has at least two vowels
            if vowel_count >= 2:
                # Add the word to the matching words list
                matching_words.append(word)

    # Return the matching words
    return matching_words