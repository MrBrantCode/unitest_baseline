"""
QUESTION:
Write a function named `count_alphabets` that takes a string as input and returns a dictionary where the keys are the unique lowercase alphabets in the string and the values are their respective frequencies. The function should have a time complexity of O(n), where n is the length of the input string, and use a constant amount of extra space.
"""

def count_alphabets(string):
    # Initialize an empty dictionary
    freq_dict = {}

    # Iterate over each character in the string
    for char in string:
        # Convert the character to lowercase
        char = char.lower()

        # Check if the character is a lowercase alphabet
        if char.isalpha() and char.islower():
            # If the character is already a key in the dictionary, increment its frequency
            if char in freq_dict:
                freq_dict[char] += 1
            # If the character is not a key in the dictionary, add it with a frequency of 1
            else:
                freq_dict[char] = 1

    return freq_dict