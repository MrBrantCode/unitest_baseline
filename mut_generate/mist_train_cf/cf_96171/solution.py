"""
QUESTION:
Create a function `character_frequency(string)` that takes a string as input, removes leading and trailing whitespace, counts the frequency of each character in the string, and returns a dictionary sorted in descending order of frequency and then alphabetically. The function should not use built-in Python functions or libraries for sorting or counting and should have a time complexity of O(n log n).
"""

def character_frequency(string):
    # Remove leading and trailing whitespace
    string = string.strip()

    # Create an empty dictionary to store the character frequencies
    frequency_dict = {}

    # Iterate over each character in the string
    for char in string:
        # Check if the character is already in the dictionary
        if char in frequency_dict:
            # If it is, increment its frequency by 1
            frequency_dict[char] += 1
        else:
            # If it is not, add it to the dictionary with a frequency of 1
            frequency_dict[char] = 1

    # Convert the dictionary to a list of tuples, where each tuple contains a character and its frequency
    frequency_list = [(char, frequency) for char, frequency in frequency_dict.items()]

    # Sort the list based on the frequency (in descending order) and then alphabetically (in ascending order)
    frequency_list.sort(key=lambda x: (-x[1], x[0]))

    # Convert the list of tuples back to a dictionary
    sorted_dict = dict(frequency_list)

    return sorted_dict