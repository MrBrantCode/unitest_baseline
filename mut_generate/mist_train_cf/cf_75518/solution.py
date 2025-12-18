"""
QUESTION:
Write a function `char_frequency` that takes a string as input and returns a dictionary containing the frequency and percentage of each alphabet character (both upper and lower case) in the string. The function should ignore special characters and numbers, and be case-insensitive, treating 'H' and 'h' as the same character. The dictionary should have the alphabet characters as keys and a tuple or single value representing the frequency or percentage of each character as values.
"""

def char_frequency(string):
    # Initialize empty dictionary to hold the character frequencies
    freq_table = {}

    # Make everything lower case to avoid dealing with case sensitivity
    string = string.lower()

    # Cycle through each character in the string
    for char in string:
        # Only deal with alphabets
        if char.isalpha():
            if char in freq_table:
                freq_table[char] += 1  # Increase count if char already in the table
            else:
                freq_table[char] = 1  # Starting count if char not in the table
                
    total_chars = sum(freq_table.values()) # Get the total number of characters

    # Transform counts into percentages
    for char in freq_table:
        freq_table[char] = (freq_table[char] / total_chars) * 100
    
    return freq_table