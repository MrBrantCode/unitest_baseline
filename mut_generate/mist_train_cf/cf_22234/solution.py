"""
QUESTION:
Write a function `character_frequency(string)` that takes a string as input and returns a dictionary where the keys are alphanumeric characters from the string and the values are their frequencies. The function should ignore non-alphanumeric characters, preserve case, and not use built-in functions or libraries that directly solve the problem. The input string is limited to 1,000 printable ASCII characters.
"""

def character_frequency(string):
    frequency_dict = {}
    for char in string:
        if char.isalnum():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    return frequency_dict