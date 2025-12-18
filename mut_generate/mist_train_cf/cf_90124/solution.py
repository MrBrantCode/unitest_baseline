"""
QUESTION:
Implement a function named `calculate_frequency` that takes a string of lowercase letters as input and returns a bitmask representing the frequency of each letter in the word. The solution should have a time complexity of O(n), where n is the length of the word, and a space complexity of O(1), meaning it should not use more space than a constant amount. The function should only use bitwise operators and not rely on any built-in functions or libraries for character manipulation.
"""

def calculate_frequency(word):
    """
    Calculate the frequency of each letter in a word as a bitmask.
    
    Parameters:
    word (str): The input word containing only lowercase letters.
    
    Returns:
    int: A bitmask representing the frequency of each letter in the word.
    """
    
    frequency = 0
    
    for char in word:
        # Calculate the bit index by subtracting the ASCII value of 'a' from the ASCII value of the current character
        bit_index = ord(char) - ord('a')
        
        # Set the corresponding bit in the frequency bitmask using the bitwise OR operator
        frequency |= (1 << bit_index)
    
    return frequency