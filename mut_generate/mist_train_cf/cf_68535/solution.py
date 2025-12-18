"""
QUESTION:
Write a Python function `evolved_histogram(test)` that takes a string of space-separated characters (including uppercase and lowercase letters, digits, and special characters) as input. The function should return a dictionary with two keys: 'highest' and 'lowest'. The value for 'highest' should be a dictionary containing characters with the highest frequency and their corresponding counts, and the value for 'lowest' should be a dictionary containing characters with the lowest frequency and their corresponding counts. All letters in the output dictionaries should be in lowercase format. In case of a tie in frequency, all tied characters should be included. The function should handle empty input strings and return a dictionary with empty dictionaries for 'highest' and 'lowest'.
"""

def entrance(test):
    """Given a string with space-separated characters (including uppercase and lowercase letters, digits, and special characters), return a dictionary with two values: 
    characters with the highest frequency and corresponding counts, and characters with the lowest frequency and corresponding counts.
    Under each category, all the letters should be displayed in lowercase format. In case of a tie in the frequency, include all the tied characters.
    """
    
    count = {}
    
    # Record the frequency of each distinct character
    for char in test:
        if char != ' ':
            char = char.lower()
            count[char] = count.get(char, 0) + 1

    # Find the highest and lowest frequency
    highest_frequency = 0 if not count else max(count.values())
    lowest_frequency = 0 if not count else min(count.values())

    # Calculate the characters with highest/lowest frequency
    characters_with_highest_freq = {char: freq for char, freq in count.items() if freq == highest_frequency}
    characters_with_lowest_freq = {char: freq for char, freq in count.items() if freq == lowest_frequency} 

    return {
        'highest': characters_with_highest_freq,
        'lowest': characters_with_lowest_freq,
    }