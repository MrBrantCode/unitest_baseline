"""
QUESTION:
Write a function `highest_frequency_letters` that finds the frequency of each letter in a given phrase and returns all the letters with the highest frequency. The phrase may contain non-alphabetical characters and the function should be case-insensitive. The function should not consider non-alphabetical characters when calculating the frequency.
"""

def highest_frequency_letters(phrase):
    """
    Finds the frequency of each letter in a given phrase and returns all the letters with the highest frequency.
    
    Parameters:
    phrase (str): The input phrase.
    
    Returns:
    list: A list of letters with the highest frequency.
    """
    
    # Convert the phrase to lower case to make the function case-insensitive
    phrase = phrase.lower()
    
    # Initialize an empty dictionary to store the frequency of each letter
    frequency = {}
    
    # Iterate over each character in the phrase
    for char in phrase:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # If the letter is already in the dictionary, increment its frequency by 1
            if char in frequency:
                frequency[char] += 1
            # If the letter is not in the dictionary, add it with a frequency of 1
            else:
                frequency[char] = 1
    
    # Find the maximum frequency
    max_frequency = max(frequency.values(), default=0)
    
    # Initialize an empty list to store the letters with the highest frequency
    highest_frequency = []
    
    # Iterate over each letter and its frequency in the dictionary
    for letter, freq in frequency.items():
        # If the frequency of the letter is equal to the maximum frequency, add it to the list
        if freq == max_frequency:
            highest_frequency.append(letter)
    
    # Return the list of letters with the highest frequency
    return highest_frequency