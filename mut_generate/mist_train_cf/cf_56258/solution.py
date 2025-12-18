"""
QUESTION:
Create a function `count_character_frequency` that takes a string `s` as input and returns a dictionary where the keys are the unique characters in the string and the values are their respective frequencies. The function should be case sensitive, meaning it treats 'H' and 'h' as different characters.
"""

def count_character_frequency(s):
    frequency = {}
    for i in s:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency