"""
QUESTION:
Write a function named `count_alphabets` that takes a string as input and returns a dictionary where the keys are the unique English alphabets (both uppercase and lowercase) in the string and the values are their respective counts. The function should ignore non-alphabet characters, have a time complexity of O(n) where n is the length of the input string, and use constant space.
"""

def count_alphabets(input_string):
    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is an English alphabet
        if char.isalpha():
            # Convert the character to lowercase to handle uppercase and lowercase letters as the same
            lowercase_char = char.lower()
            
            # Check if the letter is already in the dictionary
            if lowercase_char in letter_count:
                # If yes, increment its count
                letter_count[lowercase_char] += 1
            else:
                # If no, add it to the dictionary with a count of 1
                letter_count[lowercase_char] = 1

    return letter_count