"""
QUESTION:
Write a function `find_freq_char(s)` that identifies the alphabetic character appearing with the greatest frequency in a given string `s` containing special characters and spaces. The function should return the character with the highest frequency. Note that if there are multiple characters with the same highest frequency, any of them can be returned. The function should only consider alphabetic characters and ignore special characters and spaces.
"""

def find_freq_char(s):
    """
    Identifies the alphabetic character appearing with the greatest frequency in a given string.
    
    Parameters:
    s (str): The input string containing special characters and spaces.
    
    Returns:
    str: The character with the highest frequency.
    """
    freq = {}
    for char in s:
        if char.isalpha():  # Check if the character is alphabetic
            char = char.lower()  # Convert to lowercase for case-insensitive comparison
            if char in freq:
                freq[char] += 1
            else: 
                freq[char] = 1
    highest_freq_char = max(freq, key=freq.get)
    return highest_freq_char