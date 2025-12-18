"""
QUESTION:
Find the frequency of each letter in a given phrase and return the letter with the highest frequency. The phrase will contain letters, spaces, and punctuation marks. The function should be case-insensitive and ignore non-letter characters. Write a function named `highest_frequency_letter` that takes a string phrase as input and returns the letter with the highest frequency.
"""

def highest_frequency_letter(phrase):
    """
    Finds the frequency of each letter in a given phrase and returns the letter with the highest frequency.
    
    Parameters:
    phrase (str): The input phrase containing letters, spaces, and punctuation marks.
    
    Returns:
    str: The letter with the highest frequency in the phrase.
    """
    
    # Create a dictionary to store the frequency of each letter
    letter_frequency = {}
    
    # Iterate through each character in the phrase
    for char in phrase:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to lowercase
            char = char.lower()
            
            # Check if the character is already in the dictionary
            if char in letter_frequency:
                # Increment the count by 1
                letter_frequency[char] += 1
            else:
                # Initialize the count to 1
                letter_frequency[char] = 1
    
    # Find the letter with the highest frequency
    max_frequency = 0
    max_letter = ''
    for letter, frequency in letter_frequency.items():
        if frequency > max_frequency:
            max_frequency = frequency
            max_letter = letter
    
    # Return the letter with the highest frequency
    return max_letter