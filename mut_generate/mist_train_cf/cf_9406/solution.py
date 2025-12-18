"""
QUESTION:
Create a function `char_frequency_histogram` that takes a string as input, generates a character frequency histogram, and returns it in descending order of frequency. The function should consider only alphabetical characters and ignore case sensitivity.
"""

def char_frequency_histogram(input_string):
    """
    This function generates a character frequency histogram for the input string.
    It considers only alphabetical characters and ignores case sensitivity.
    The histogram is returned in descending order of frequency.

    Parameters:
    input_string (str): The input string for which the frequency histogram is generated.

    Returns:
    dict: A dictionary containing the characters as keys and their frequencies as values.
    """
    # Convert the string to lower case to ignore case sensitivity
    input_string = input_string.lower()
    
    # Initialize an empty dictionary to store the frequency of each character
    frequency_histogram = {}
    
    # Iterate over each character in the string
    for char in input_string:
        # Check if the character is an alphabet
        if char.isalpha():
            # If the character is already in the dictionary, increment its count
            if char in frequency_histogram:
                frequency_histogram[char] += 1
            # If the character is not in the dictionary, add it with a count of 1
            else:
                frequency_histogram[char] = 1
    
    # Sort the dictionary by frequency in descending order
    frequency_histogram = dict(sorted(frequency_histogram.items(), key=lambda item: item[1], reverse=True))
    
    return frequency_histogram