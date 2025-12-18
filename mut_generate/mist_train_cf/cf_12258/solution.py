"""
QUESTION:
Create a function named `count_alphabet_frequency` that calculates the frequency of alphabets in a given string, ignoring case, spaces, special characters, and numbers. The function should return a dictionary where the keys are the unique alphabets and the values are their respective frequencies. The function should treat 'a' and 'A' as the same character.
"""

def count_alphabet_frequency(input_string):
    frequency = {}
    input_string = input_string.lower()
    for char in input_string:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency