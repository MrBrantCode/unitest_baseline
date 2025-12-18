"""
QUESTION:
Write a function named `calculate_frequency` that calculates the frequency of each letter in a given word. The function should use a bitmask to keep track of the frequency, have a time complexity of O(n), and a space complexity of O(1), where n is the length of the word. It should only contain lowercase alphabets (a-z) and should not use any built-in functions or libraries for character manipulation.
"""

def calculate_frequency(word):
    frequency = 0
    
    for char in word:
        bit_index = ord(char) - ord('a')
        frequency |= (1 << bit_index)
    
    return frequency