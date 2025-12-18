"""
QUESTION:
Create a function named `count_alphabets` that takes a string as input and returns a list of tuples, where each tuple contains an alphabet character and its frequency in the string. The function should ignore case sensitivity, consider only lowercase characters, and return the list in descending order of frequency.
"""

def count_alphabets(string):
    # Convert the string to lowercase
    string = string.lower()

    # Initialize a dictionary to store the frequency of each character
    frequency = {}

    # Iterate over each character in the string
    for char in string:
        # Check if the character is an alphabet
        if char.isalpha():
            # Update the frequency of the character
            frequency[char] = frequency.get(char, 0) + 1

    # Sort the frequency dictionary in descending order of values
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return sorted_frequency