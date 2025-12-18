"""
QUESTION:
Create a function called `calculate_letter_frequency` that takes a string `word` as input and returns a dictionary where the keys are the unique letters in the word and the values are their corresponding frequencies. The function should iterate over the word only once.
"""

def calculate_letter_frequency(word):
    frequency = {}
    for letter in word:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency