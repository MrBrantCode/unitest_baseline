"""
QUESTION:
Create a function named `character_frequency` that takes a string as input and returns a dictionary. The dictionary should contain each unique character in the string as keys and their frequencies as values. The function should ignore case sensitivity and whitespace characters. The time complexity of the function should be O(n), where n is the length of the string.
"""

def character_frequency(string):
    frequency_dict = {}
    string = string.replace(" ", "").lower()
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict