"""
QUESTION:
Implement the function `generate_frequency_table(sequence)` to create a frequency table for a given sequence of printable ASCII characters with a maximum length of 10^6 characters. The function should use a dictionary data structure and have a time complexity of O(n), where n is the length of the input sequence. The output should be a dictionary where the keys are the characters from the sequence and the values are their corresponding frequencies.
"""

def generate_frequency_table(sequence):
    frequency_table = {}
    for char in sequence:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    return frequency_table