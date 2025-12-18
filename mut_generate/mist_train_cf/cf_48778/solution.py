"""
QUESTION:
Create a function named 'letter_frequency' that calculates the frequency rate of each unique alphabetical character in a given string. The function should return a dictionary where the keys are the unique characters and the values represent their frequencies. The function should be case sensitive and consider 'a' and 'A' as different characters.
"""

def letter_frequency(sentence):
    frequency = {}
    for letter in sentence:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency