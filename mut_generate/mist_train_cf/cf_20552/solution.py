"""
QUESTION:
Create a function named `character_frequency` that takes a string as input and returns a dictionary containing the characters from the string as keys and their frequency in the string as values. The function should sort the dictionary in descending order based on the frequency of each character, and for characters with the same frequency, sort them alphabetically. The function should ignore leading and trailing whitespace in the string, handle strings with multiple lines, and have a time complexity of O(n log n), where n is the length of the string, without using any built-in Python functions or libraries for sorting or counting.
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