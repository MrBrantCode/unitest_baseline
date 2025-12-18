"""
QUESTION:
Create a function named `find_distinctive_char(s)` that takes a string `s` as input and returns a tuple containing the distinctive character and its index location. The distinctive character is defined as the first unique character in the string. If all characters are repeating, the distinctive character is the least frequent character. In case of a tie, the function should return the first character from the tie characters. The function should be case sensitive and treat special characters the same as regular letters.
"""

def find_distinctive_char(s):
    freq_dict = {}

    # Create a frequency distribution table for all characters
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    # Find the first unique character
    for char in s:
        if freq_dict[char] == 1:
            return char, s.index(char)
    
    # In case all characters are repeating, return the least frequent character
    least_freq_char = min(freq_dict, key=freq_dict.get)
    return least_freq_char, s.index(least_freq_char)