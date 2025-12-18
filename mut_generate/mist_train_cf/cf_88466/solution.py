"""
QUESTION:
Write a function `count_alphabets` that takes a string as input and returns a dictionary with the count of each unique English alphabet in the string, ignoring punctuation marks, special characters, and spaces. The function should consider uppercase and lowercase letters as separate entities and have a time complexity of O(n), where n is the length of the input string, using only constant space.
"""

def count_alphabets(input_string):
    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an English alphabet
        if char.isalpha():
            # Use the original character to handle uppercase and lowercase letters as separate entities
            if char in letter_count:
                # If yes, increment its count
                letter_count[char] += 1
            else:
                # If no, add it to the dictionary with a count of 1
                letter_count[char] = 1

    return letter_count